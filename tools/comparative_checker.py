#!/usr/bin/env python3
import json
from pathlib import Path

REQUIRED_FILES = [
    "COMPARATIVE_ANALYSIS.md",
    "DIFFERENCE_MATRIX.md",
    "LOT_ADDED_VALUE.md",
    "docs/EXTERNAL_REVIEW_PACKET.md",
    "examples/comparative_frameworks.json",
]

REQUIRED_PHRASES = {
    "COMPARATIVE_ANALYSIS.md": [
        "Many neighboring frameworks already capture parts of the same failure pattern.",
        "compression, generalization, and operational transfer",
        "local correctness from valid use",
        "Hostile Reviewer Questions",
        "It is not enough for final validation."
    ],
    "DIFFERENCE_MATRIX.md": [
        "overclaiming novelty",
        "underclaiming the compression",
        "LOT does not produce domain expertise by itself.",
        "It provides the slot where the missing dependency must be exposed."
    ],
    "LOT_ADDED_VALUE.md": [
        "local correctness becomes invalid use",
        "It does not add the idea that",
        "This is the anti-hallucination property of the framework."
    ],
    "docs/EXTERNAL_REVIEW_PACKET.md": [
        "I am looking for criticism, not endorsement.",
        "External review is not validation hunting.",
        "attack surface discovery"
    ]
}

FORBIDDEN_PHRASES = [
    "replaces existing disciplines",
    "proves all concrete errors",
    "universal scientific law",
    "theory of everything",
    "solves everything",
    "99%"
]

def main():
    for rel in REQUIRED_FILES:
        path = Path(rel)
        if not path.exists():
            raise SystemExit(f"Missing required file: {rel}")
        if not path.read_text(encoding="utf-8").strip():
            raise SystemExit(f"Empty required file: {rel}")

    for rel, phrases in REQUIRED_PHRASES.items():
        text = Path(rel).read_text(encoding="utf-8")
        missing = [p for p in phrases if p not in text]
        if missing:
            raise SystemExit(f"{rel} missing required phrases: {missing}")

    all_text = ""
    for rel in REQUIRED_FILES:
        if rel.endswith(".md"):
            all_text += "\n" + Path(rel).read_text(encoding="utf-8").lower()

    forbidden_found = []
    for phrase in FORBIDDEN_PHRASES:
        if phrase.lower() in all_text:
            forbidden_found.append(phrase)

    if forbidden_found:
        raise SystemExit(f"Forbidden overclaim phrases found: {forbidden_found}")

    data = json.loads(Path("examples/comparative_frameworks.json").read_text(encoding="utf-8"))
    frameworks = data.get("frameworks", [])
    if len(frameworks) < 7:
        raise SystemExit(f"Expected at least 7 frameworks, found {len(frameworks)}")

    required_keys = [
        "id",
        "name",
        "field",
        "captures",
        "near_overlap",
        "gap_or_difference",
        "lot_added_value",
        "fair_verdict",
    ]

    ids = set()
    for fw in frameworks:
        missing = [k for k in required_keys if k not in fw]
        if missing:
            raise SystemExit(f"Framework missing keys: {fw.get('id', '<no id>')} {missing}")
        if fw["id"] in ids:
            raise SystemExit(f"Duplicate framework id: {fw['id']}")
        ids.add(fw["id"])
        for key in ["captures", "near_overlap", "gap_or_difference", "lot_added_value"]:
            if not isinstance(fw[key], list) or len(fw[key]) < 2:
                raise SystemExit(f"Framework {fw['id']} has weak list field: {key}")

    names = {fw["id"] for fw in frameworks}
    must_have = {
        "nist_ai_rmf",
        "model_risk_management",
        "stamp_stpa",
        "map_territory",
        "systems_thinking",
    }
    missing_must = sorted(must_have - names)
    if missing_must:
        raise SystemExit(f"Missing required neighboring frameworks: {missing_must}")

    print(f"PASS comparative frameworks: {len(frameworks)}")
    print("PASS required comparative files")
    print("PASS required phrases")
    print("PASS overclaim discipline")
    print("All comparative analysis checks passed.")

if __name__ == "__main__":
    main()
