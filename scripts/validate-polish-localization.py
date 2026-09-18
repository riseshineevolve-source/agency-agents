#!/usr/bin/env python3
"""Regression validator for accepted RSE Polish localization fixtures.

Scans only final child-facing Polish candidate sections from accepted fixtures.
Historical/candidate calibration files are intentionally excluded.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ACCEPTED = [
    ROOT / "localization/pl-PL/golden-tests/published-book-calibration-round2.md",
    ROOT / "localization/pl-PL/golden-tests/published-book-calibration-round3.md",
    ROOT / "localization/pl-PL/golden-tests/published-book-controlled-pilot-day11.md",
    ROOT / "localization/pl-PL/golden-tests/published-book-bounded-batch-days05-20-25.md",
    ROOT / "localization/pl-PL/golden-tests/gentle-steps-christmas-calibration-round1.md",
    ROOT / "localization/pl-PL/golden-tests/gentle-steps-christmas-week1-controlled-expansion.md",
]

AIISMS = ROOT / "localization/pl-PL/FORBIDDEN_AIISMS_PL.yml"

CHRISTMAS_CALIBRATION_LABELS = [
    "SPOKOJNA CHWILA",
    "ISKRA ZABAWY",
    "CHWILA BLISKOŚCI",
]

REQUIRED_LOCKED_LABELS = [
    "NIEZBĘDNIK",
    "MISJA",
    "TAJNY PATENT",
    "MINI-MISJA",
    "CO TU SIĘ DZIEJE?",
    "TERAZ TY TWORZYSZ!",
    "MAŁY KROK NA DZIŚ",
    "CHWILA NA ODDECH",
    "STREFA ZABAWY",
    "INSTRUKCJA BEZ SPINY",
    "MISJA DNIA",
    "TAJNA TARCZA",
]

ENGLISH_LABELS = [
    "THE GENTLE WHY",
    "YOUR TURN TO CREATE",
    "GENTLE STEP",
    "PAUSE & BREATHE",
    "PLAY ZONE",
    "SECRET SHIELD",
    "NO-STRESS MANUAL",
]

REGRESSION_BANS = [
    "Kapitan(a)",
    "gotowy/gotowa",
    "zrobiłeś(-aś)",
    "Dealer smakołyków",
    "Stabilizator nastroju",
    "RADAR ŻYCZLIWOŚCI",
    "zerowy limit baterii",
]

# Direct second-person forms that unnecessarily force gender in child-facing Polish.
GENDERED_DIRECT_RE = re.compile(
    r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+"
    r"(?:nąłeś|nęłaś|iłeś|iłaś|yłeś|yłaś|łeś|łaś|łbyś|łabyś)\b",
    re.IGNORECASE,
)

HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")


def extract_final_sections(text: str) -> str:
    """Return only final Polish candidate prose, excluding QA/source commentary."""
    lines = text.splitlines()
    out: list[str] = []
    in_final = False
    start_level = 0

    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip().lower()

            if (
                "final pl candidate" in title
                or title == "final pl"
                or title == "pl candidate"
            ):
                in_final = True
                start_level = level
                continue

            if in_final and level <= start_level and any(
                stop in title
                for stop in (
                    "qa",
                    "source functions",
                    "immutable",
                    "review",
                    "engine findings",
                    "batch regression",
                )
            ):
                in_final = False

        if in_final:
            out.append(line)

    return "\n".join(out)


def load_aiisms() -> list[str]:
    if not AIISMS.exists():
        return []
    phrases: list[str] = []
    for line in AIISMS.read_text(encoding="utf-8").splitlines():
        match = re.match(r'^\s*-\s*"([^"]+)"\s*$', line)
        if match:
            phrases.append(match.group(1))
    return phrases


def line_number(text: str, needle: str) -> int:
    idx = text.lower().find(needle.lower())
    if idx < 0:
        return 0
    return text.count("\n", 0, idx) + 1


def main() -> int:
    errors: list[str] = []
    combined: list[str] = []

    for path in ACCEPTED:
        if not path.exists():
            errors.append(f"MISSING accepted fixture: {path.relative_to(ROOT)}")
            continue

        raw = path.read_text(encoding="utf-8")
        final = extract_final_sections(raw)
        rel = path.relative_to(ROOT)

        if not final.strip():
            errors.append(f"NO final PL sections extracted: {rel}")
            continue

        combined.append(final)

        for match in GENDERED_DIRECT_RE.finditer(final):
            errors.append(
                f"GENDERED direct-address form in {rel}: {match.group(0)!r} "
                f"(candidate line {line_number(final, match.group(0))})"
            )

        low = final.lower()

        for phrase in REGRESSION_BANS:
            if phrase.lower() in low:
                errors.append(f"REGRESSION phrase in {rel}: {phrase!r}")

        for phrase in ENGLISH_LABELS:
            if phrase.lower() in low:
                errors.append(f"ENGLISH recurring label leaked into {rel}: {phrase!r}")

    corpus = "\n".join(combined)
    corpus_low = corpus.lower()

    for label in REQUIRED_LOCKED_LABELS:
        if label.lower() not in corpus_low:
            errors.append(f"LOCKED label missing from accepted corpus: {label!r}")

    for label in CHRISTMAS_CALIBRATION_LABELS:
        if label.lower() not in corpus_low:
            errors.append(f"CHRISTMAS calibration label missing from accepted corpus: {label!r}")

    for phrase in load_aiisms():
        if phrase.lower() in corpus_low:
            errors.append(f"FORBIDDEN AI/translationese phrase in accepted corpus: {phrase!r}")

    if errors:
        print("RSE Polish localization regression: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RSE Polish localization regression: PASS")
    print(f"Accepted fixtures checked: {len(ACCEPTED)}")
    print(f"Final candidate characters checked: {len(corpus)}")
    print(f"Locked labels verified: {len(REQUIRED_LOCKED_LABELS)}")
    print(f"Christmas calibration labels verified: {len(CHRISTMAS_CALIBRATION_LABELS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
