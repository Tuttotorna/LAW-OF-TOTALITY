#!/usr/bin/env python3
from pathlib import Path

REQUIRED_FILES = [
    "CLAIMS_FREEZE.md",
    "EXTERNAL_REVIEW_RELEASE.md",
    "RELEASE_NOTES_v1.0.0.md",
    "REVIEW_FILE_MAP.md",
    "docs/FIRST_REVIEWER_SUBMISSIONS.md",
    "docs/V1_PUBLIC_STATEMENT.md",
    "docs/V1_REVIEW_PROTOCOL.md",
]

REQUIRED_PHRASES = {
    "CLAIMS_FREEZE.md": [
        "local correctness does not imply valid use",
        "This is the version to attack.",
        "not externally validated yet"
    ],
    "EXTERNAL_REVIEW_RELEASE.md": [
        "external review release",
        "Validation status: not externally validated",
        "Ask reviewers for failure points."
    ],
    "RELEASE_NOTES_v1.0.0.md": [
        "Law of Totality v1.0.0",
        "This is the first external review release",
        "This is the version to attack."
    ],
    "REVIEW_FILE_MAP.md": [
        "Fast Review Path",
        "Minimal Review",
        "Hostile Review"
    ],
    "docs/FIRST_REVIEWER_SUBMISSIONS.md": [
        "one reviewer class at a time",
        "Do not broadcast.",
        "Start with AI safety / AI governance or model risk."
    ],
    "docs/V1_PUBLIC_STATEMENT.md": [
        "pre-validation external review release",
        "asking for criticism, not endorsement",
        "It needs attack surface."
    ],
    "docs/V1_REVIEW_PROTOCOL.md": [
        "Convert Every Serious Criticism Into An Issue",
        "No expansion before review response.",
        "v1.1.0 Review Response Release"
    ],
}

FORBIDDEN_PHRASES = [
    "theory of everything",
    "solves everything",
    "scientifically proven universal law",
    "universal scientific law",
    "proves all errors",
    "replaces existing disciplines",
    "final theory",
    "settled truth",
    "validated universal law",
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
        all_text += "\n" + Path(rel).read_text(encoding="utf-8").lower()

    bad = [phrase for phrase in FORBIDDEN_PHRASES if phrase.lower() in all_text]
    if bad:
        raise SystemExit(f"Forbidden phrase found: {bad}")

    readme = Path("README.md")
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        required_readme = [
            "v1.0.0 External Review Release",
            "claim freeze",
            "external review release",
            "This is the version to attack."
        ]
        missing = [p for p in required_readme if p not in readme_text]
        if missing:
            raise SystemExit(f"README missing v1.0.0 phrases: {missing}")

    print("PASS v1.0.0 release files")
    print("PASS claim freeze")
    print("PASS external review framing")
    print("PASS overclaim discipline")
    print("All v1.0.0 release checks passed.")

if __name__ == "__main__":
    main()
