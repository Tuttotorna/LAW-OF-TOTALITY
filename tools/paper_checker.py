#!/usr/bin/env python3
from pathlib import Path

REQUIRED_FILES = [
    "PAPER_SHORT.md",
    "docs/ABSTRACT.md",
    "docs/SUBMISSION_LETTER.md",
    "docs/REVIEW_TARGETS.md",
]

REQUIRED_PHRASES = {
    "PAPER_SHORT.md": [
        "The Structural Error Formula",
        "local correctness does not imply valid use",
        "ErrΩ(x,F,U)",
        "What the Formula Does Not Claim",
        "Negative Controls",
        "Relation to Existing Frameworks",
        "Current Status",
        "Review Request",
        "attack surface discovery"
    ],
    "docs/ABSTRACT.md": [
        "local correctness does not imply valid use",
        "candidate cross-domain audit layer",
        "ready for hostile review"
    ],
    "docs/SUBMISSION_LETTER.md": [
        "Please attack the framework rather than endorse it.",
        "whether the formula survives technical criticism"
    ],
    "docs/REVIEW_TARGETS.md": [
        "What Not To Ask",
        "Ask reviewers to find failure.",
        "strongest existing equivalent"
    ]
}

FORBIDDEN_PHRASES = [
    "theory of everything",
    "solves everything",
    "99%",
    "scientifically proven universal law",
    "universal scientific law",
    "proves all errors",
    "replaces existing disciplines",
    "final theory",
    "settled truth"
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
        raise SystemExit(f"Forbidden overclaim phrases found: {bad}")

    paper = Path("PAPER_SHORT.md").read_text(encoding="utf-8")
    sections = [line for line in paper.splitlines() if line.startswith("## ")]
    if len(sections) < 10:
        raise SystemExit(f"Expected at least 10 paper sections, found {len(sections)}")

    references_required = [
        "NIST",
        "Federal Reserve",
        "Office of the Comptroller of the Currency",
        "STPA Handbook",
        "Korzybski",
    ]
    missing_refs = [r for r in references_required if r not in paper]
    if missing_refs:
        raise SystemExit(f"Missing reference markers: {missing_refs}")

    word_count = len(paper.split())
    if word_count < 1800:
        raise SystemExit(f"Paper too short: {word_count} words")
    if word_count > 4500:
        raise SystemExit(f"Paper too long for v0.8.0 short-paper target: {word_count} words")

    print(f"PASS paper word count: {word_count}")
    print("PASS required paper files")
    print("PASS required phrases")
    print("PASS reference markers")
    print("PASS overclaim discipline")
    print("All short-paper checks passed.")

if __name__ == "__main__":
    main()
