"""Machine guards for native Polish re-authoring from source function.

The engine does not write prose. It enforces provenance, stage order and the
critical source-visibility boundary: the native Polish first writer receives a
functional brief, not sentence-level English source copy.
"""
from __future__ import annotations

from pathlib import Path

from .contracts import require
from .io import digest, file_digest

FORBIDDEN_BRIEF_KEYS = {
    "source_text", "source_sentence", "source_paragraph", "source_excerpt",
    "english_copy", "literal_translation", "draft_pl", "target_text",
}
REQUIRED_UNIT_FIELDS = {
    "id", "source_locator", "surface_type", "audience", "function",
    "mechanics", "immutable_facts", "character_roles",
    "safety_claim_boundaries", "tone_job",
}


def _walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_keys(child)


def validate_profile(profile):
    require(profile.get("version") == 1, "Unsupported re-authoring profile version")
    require(profile.get("mode") == "native_reauthor_from_function",
            "Re-authoring profile must use native_reauthor_from_function")
    require(bool(profile.get("product")), "Re-authoring profile product missing")
    require(profile.get("source_language") == "en" and profile.get("target_language") == "pl-PL",
            "Re-authoring profile must be en -> pl-PL")
    stages = profile.get("stages", [])
    require(isinstance(stages, list) and len(stages) == len(set(stages)) and stages,
            "Re-authoring stages must be unique and non-empty")
    require(stages[0] == "source_function_analysis" and "native_polish_first_write" in stages,
            "Re-authoring must start with source-function analysis and include native first-write")
    require(profile.get("native_writer_source_visibility") == "functional_brief_only",
            "Native writer must be isolated from sentence-level English source")
    reviews = profile.get("required_review_stages", [])
    require(isinstance(reviews, list) and reviews and set(reviews) <= set(stages),
            "Required review stages must be declared stages")
    gates = profile.get("owner_gates", [])
    require(isinstance(gates, list) and all(isinstance(g, str) and g for g in gates),
            "Owner gates must be named")
    return profile


def init_run(source_file, source_revision, profile):
    validate_profile(profile)
    source_file = str(source_file)
    require(bool(source_revision), "Source revision required")
    require(Path(source_file).is_file(), "Source file does not exist")
    return {
        "format": "rse-reauthor-run-v1",
        "product": profile["product"],
        "mode": profile["mode"],
        "source_language": "en",
        "target_language": "pl-PL",
        "source_file": source_file,
        "source_revision": source_revision,
        "source_sha256": file_digest(source_file),
        "profile_sha256": digest(profile),
        "native_writer_source_visibility": "functional_brief_only",
        "current_stage": "source_function_analysis",
        "stages": list(profile["stages"]),
    }


def validate_run(run, profile, verify_source=True):
    validate_profile(profile)
    require(run.get("format") == "rse-reauthor-run-v1", "Wrong re-authoring run format")
    require(run.get("product") == profile["product"] and run.get("mode") == profile["mode"],
            "Run/profile mismatch")
    require(run.get("profile_sha256") == digest(profile), "Run uses stale re-authoring profile")
    require(run.get("native_writer_source_visibility") == "functional_brief_only",
            "Run weakened native-writer source isolation")
    require(run.get("stages") == profile["stages"], "Run stage contract drifted")
    if verify_source:
        require(Path(run["source_file"]).is_file(), "Run source file unavailable")
        require(run.get("source_sha256") == file_digest(run["source_file"]),
                "English source bytes changed; start a new run or re-authorize the revision")
    return run


def validate_functional_brief(run, profile, brief):
    validate_run(run, profile, verify_source=False)
    require(brief.get("format") == "rse-functional-brief-v1", "Wrong functional brief format")
    require(brief.get("product") == run["product"], "Functional brief product mismatch")
    require(brief.get("source_sha256") == run["source_sha256"], "Functional brief uses stale English source")
    require(brief.get("profile_sha256") == run["profile_sha256"], "Functional brief uses stale profile")
    forbidden = sorted(set(_walk_keys(brief)) & FORBIDDEN_BRIEF_KEYS)
    require(not forbidden, f"Functional brief leaks sentence-level source/target copy: {forbidden}")
    units = brief.get("units", [])
    require(isinstance(units, list) and units, "Functional brief must contain units")
    ids = set()
    for unit in units:
        missing = REQUIRED_UNIT_FIELDS - set(unit)
        require(not missing, f"Functional brief unit missing fields: {sorted(missing)}")
        sid = unit["id"]
        require(isinstance(sid, str) and sid and sid not in ids, f"Invalid/duplicate unit id: {sid!r}")
        ids.add(sid)
        require(isinstance(unit["source_locator"], str) and unit["source_locator"].strip(),
                f"Source locator missing: {sid}")
        for field in ("function", "tone_job", "surface_type", "audience"):
            require(isinstance(unit[field], str) and unit[field].strip(), f"Missing {field}: {sid}")
        for field in ("mechanics", "immutable_facts", "character_roles", "safety_claim_boundaries"):
            require(isinstance(unit[field], list) and all(isinstance(x, str) and x.strip() for x in unit[field]),
                    f"Invalid {field}: {sid}")
        require(unit.get("wording_is_disposable") is True,
                f"Functional brief must explicitly mark English wording disposable: {sid}")
    return brief


def writer_packet(run, profile, brief):
    validate_functional_brief(run, profile, brief)
    allowed = (
        "id", "surface_type", "audience", "function", "mechanics", "immutable_facts",
        "character_roles", "safety_claim_boundaries", "tone_job", "humor_room",
        "cultural_friction", "recurrence_context",
    )
    units = [{key: unit[key] for key in allowed if key in unit} for unit in brief["units"]]
    packet = {
        "format": "rse-native-pl-writer-packet-v1",
        "product": run["product"],
        "run_sha256": digest(run),
        "brief_sha256": digest(brief),
        "authoring_mode": "from_function_not_from_english_wording",
        "source_visibility": "functional_brief_only",
        "instructions": [
            "Write as if the Polish product were created in Poland from the beginning.",
            "Preserve mechanics, facts, character roles, safety and claim boundaries.",
            "Do not reconstruct English metaphors, sentence order or motivational cadence.",
            "Prefer concrete contemporary family Polish, situational humor and spoken rhythm.",
            "Avoid corporate coaching, therapy-speak, imported mindfulness phrasing and forced youth slang.",
        ],
        "units": units,
    }
    require(not (set(_walk_keys(packet)) & FORBIDDEN_BRIEF_KEYS),
            "Writer packet leaked source/target copy fields")
    return packet


def validate_candidate(packet, candidate):
    require(packet.get("format") == "rse-native-pl-writer-packet-v1", "Wrong writer packet format")
    require(candidate.get("format") == "rse-native-pl-candidate-v1", "Wrong candidate format")
    require(candidate.get("product") == packet["product"], "Candidate product mismatch")
    require(candidate.get("brief_sha256") == packet["brief_sha256"], "Candidate uses stale functional brief")
    require(candidate.get("authoring_basis") == "functional_brief_only",
            "Candidate must attest functional-brief-only first-write")
    units = candidate.get("units", [])
    expected = [u["id"] for u in packet["units"]]
    require([u.get("id") for u in units] == expected, "Candidate unit IDs/order must match writer packet")
    for unit in units:
        require(isinstance(unit.get("draft_pl"), str) and unit["draft_pl"].strip(),
                f"Empty Polish first-write: {unit.get('id')}")
    return candidate


def backcheck_packet(run, profile, brief, packet, candidate):
    validate_functional_brief(run, profile, brief)
    validate_candidate(packet, candidate)
    brief_by_id = {u["id"]: u for u in brief["units"]}
    target_by_id = {u["id"]: u["draft_pl"] for u in candidate["units"]}
    return {
        "format": "rse-reauthor-backcheck-packet-v1",
        "product": run["product"],
        "source_file": run["source_file"],
        "source_revision": run["source_revision"],
        "source_sha256": run["source_sha256"],
        "candidate_sha256": digest(candidate),
        "instruction": (
            "Re-open the English source only now. Verify mechanics, facts, counts, sequence, consent, "
            "claim strength, character continuity and required function. Do not rewrite Polish toward "
            "English syntax, metaphors or cadence merely to make the texts look parallel."
        ),
        "units": [
            {
                "id": sid,
                "source_locator": brief_by_id[sid]["source_locator"],
                "function": brief_by_id[sid]["function"],
                "mechanics": brief_by_id[sid]["mechanics"],
                "immutable_facts": brief_by_id[sid]["immutable_facts"],
                "safety_claim_boundaries": brief_by_id[sid]["safety_claim_boundaries"],
                "final_pl_for_review": target_by_id[sid],
            }
            for sid in [u["id"] for u in brief["units"]]
        ],
    }


def final_gate(run, profile, packet, candidate, reviews):
    validate_run(run, profile, verify_source=False)
    validate_candidate(packet, candidate)
    candidate_sha = digest(candidate)
    require(reviews.get("format") == "rse-reauthor-review-bundle-v1", "Wrong review bundle format")
    require(reviews.get("candidate_sha256") == candidate_sha, "Reviews are stale for this Polish candidate")
    by_stage = {r.get("stage"): r for r in reviews.get("reviews", [])}
    missing = [s for s in profile["required_review_stages"] if s not in by_stage]
    require(not missing, f"Missing required re-authoring reviews: {missing}")
    failures = []
    for stage in profile["required_review_stages"]:
        review = by_stage[stage]
        if review.get("status") != "PASS" or not review.get("reviewer"):
            failures.append(stage)
        require(review.get("candidate_sha256") == candidate_sha, f"Stale review receipt: {stage}")
    if failures:
        return {"status": "BLOCK", "failed_review_stages": failures, "candidate_sha256": candidate_sha}
    decisions = reviews.get("owner_decisions", {})
    unresolved = [gate for gate in profile.get("owner_gates", [])
                  if decisions.get(gate, {}).get("status") != "APPROVED"
                  or decisions.get(gate, {}).get("candidate_sha256") != candidate_sha]
    return {
        "status": "READY_FOR_OWNER_GATE" if unresolved else "PASS",
        "candidate_sha256": candidate_sha,
        "unresolved_owner_gates": unresolved,
    }
