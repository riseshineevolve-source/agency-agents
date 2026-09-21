"""Strict JSON/YAML IO and RFC 6901 paths. Never infer translatable keys."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


class ContractError(ValueError):
    pass


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if not isinstance(key, str):
            raise ContractError("Object keys must be strings")
        if key in result:
            raise ContractError(f"Duplicate key: {key}")
        result[key] = value
    return result


def load(path):
    path = Path(path)
    raw = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml
        except ImportError as exc:
            raise ContractError("Install scripts/localization/requirements.txt for YAML input") from exc

        class StrictLoader(yaml.SafeLoader):
            pass

        def mapping(loader, node):
            return unique_pairs((loader.construct_object(k), loader.construct_object(v)) for k, v in node.value)

        StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
        # RSE metadata uses unquoted ISO dates. Keep their exact scalar spelling
        # as text instead of creating Python-only datetime objects.
        StrictLoader.add_constructor("tag:yaml.org,2002:timestamp", lambda loader, node: loader.construct_scalar(node))
        data = yaml.load(raw, Loader=StrictLoader)
    else:
        data = json.loads(raw, object_pairs_hook=unique_pairs)
    try:
        canonical(data)
    except (TypeError, ValueError) as exc:
        raise ContractError("Use JSON-compatible YAML values (quote dates and numeric keys)") from exc
    return data


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8", newline="\n")


def escape(key):
    return str(key).replace("~", "~0").replace("/", "~1")


def parts(pointer):
    if pointer == "":
        return []
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ContractError(f"Invalid JSON pointer: {pointer!r}")
    import re
    if re.search(r"~(?![01])", pointer):
        raise ContractError(f"Malformed JSON pointer escape: {pointer}")
    return [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")]


def get(document, pointer):
    value = document
    try:
        for key in parts(pointer):
            if isinstance(value, list):
                if not key.isdigit() or str(int(key)) != key:
                    raise ContractError(f"Invalid list index: {pointer}")
                value = value[int(key)]
            else:
                value = value[key]
    except (KeyError, IndexError, TypeError) as exc:
        raise ContractError(f"Source path does not exist: {pointer}") from exc
    return value


def put(document, pointer, value):
    keys = parts(pointer)
    if not keys:
        return value
    parent = document
    for key in keys[:-1]:
        parent = parent[int(key)] if isinstance(parent, list) else parent[key]
    key = int(keys[-1]) if isinstance(parent, list) else keys[-1]
    parent[key] = value
    return document


def leaves(value, pointer=""):
    if isinstance(value, dict):
        for key in sorted(value):
            yield from leaves(value[key], pointer + "/" + escape(key))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from leaves(item, pointer + "/" + str(i))
    else:
        yield pointer, value
