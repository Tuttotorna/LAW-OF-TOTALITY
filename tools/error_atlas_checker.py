#!/usr/bin/env python3
import json
from pathlib import Path

REQUIRED_FIELDS = [
    "id",
    "domain",
    "title",
    "x",
    "F",
    "U",
    "valid_scope",
    "excluded_critical_dependencies",
    "structural_error",
    "correction",
    "trajectory_change",
]

FORBIDDEN_PHRASES = [
    "solves everything",
    "proves every error",
    "99%",
    "scientifically proven universal law",
]

def main():
    json_path = Path("examples/error_atlas_cases.json")
    md_path = Path("ERROR_ATLAS.md")

    if not json_path.exists():
        raise SystemExit("Missing examples/error_atlas_cases.json")
    if not md_path.exists():
        raise SystemExit("Missing ERROR_ATLAS.md")

    data = json.loads(json_path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])

    if len(cases) < 40:
        raise SystemExit(f"Expected at least 40 cases, found {len(cases)}")

    ids = set()
    domains = set()
    positives = 0
    negatives = 0

    for idx, case in enumerate(cases, 1):
        missing = [field for field in REQUIRED_FIELDS if field not in case]
        if missing:
            raise SystemExit(f"Case {idx} missing fields: {missing}")

        if not case["id"] or case["id"] in ids:
            raise SystemExit(f"Duplicate or empty id at case {idx}: {case.get('id')}")
        ids.add(case["id"])

        if not isinstance(case["excluded_critical_dependencies"], list):
            raise SystemExit(f"excluded_critical_dependencies must be a list in case {case['id']}")

        domains.add(case["domain"])
        if case["structural_error"]:
            positives += 1
        else:
            negatives += 1

    if len(domains) < 15:
        raise SystemExit(f"Expected at least 15 represented domains, found {len(domains)}")

    if positives < 30:
        raise SystemExit(f"Expected at least 30 positive structural-error cases, found {positives}")

    if negatives < 5:
        raise SystemExit(f"Expected at least 5 negative controls, found {negatives}")

    md = md_path.read_text(encoding="utf-8")
    for phrase in FORBIDDEN_PHRASES:
        if phrase.lower() in md.lower():
            raise SystemExit(f"Forbidden overclaim phrase found in ERROR_ATLAS.md: {phrase}")

    required_md_phrases = [
        "The law does not explain every thing as total content.",
        "It explains the structural validity of every finite treatment submitted to it.",
        "Negative control cases",
        "Core Formula",
    ]

    missing_md = [p for p in required_md_phrases if p not in md]
    if missing_md:
        raise SystemExit(f"ERROR_ATLAS.md missing required phrases: {missing_md}")

    print(f"PASS Error Atlas cases: {len(cases)}")
    print(f"PASS Domains represented: {len(domains)}")
    print(f"PASS Positive cases: {positives}")
    print(f"PASS Negative controls: {negatives}")
    print("All Error Atlas checks passed.")

if __name__ == "__main__":
    main()
