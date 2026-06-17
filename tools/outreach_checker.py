#!/usr/bin/env python3
from pathlib import Path

REQUIRED_FILES = [
    "TECHNICAL_SUMMARY.md",
    "docs/OUTREACH_EMAIL_GENERAL.md",
    "docs/OUTREACH_EMAIL_AI.md",
    "docs/OUTREACH_EMAIL_MODEL_RISK.md",
    "docs/OUTREACH_EMAIL_SYSTEMS.md",
    "REVIEWER_CHECKLIST.md",
    "REVIEW_QUESTIONS.md",
    "docs/GITHUB_REVIEW_GUIDE.md",
    "docs/OUTREACH_PLAN.md",
    ".github/ISSUE_TEMPLATE/counterexample.md",
    ".github/ISSUE_TEMPLATE/definition_weakness.md",
    ".github/ISSUE_TEMPLATE/existing_framework_equivalent.md",
    ".github/ISSUE_TEMPLATE/case_atlas_objection.md",
    ".github/ISSUE_TEMPLATE/operational_use_case.md",
]

REQUIRED_PHRASES = {
    "TECHNICAL_SUMMARY.md": [
        "local correctness does not imply valid use",
        "Ready for hostile review.",
        "correct inside F ≠ valid for U",
        "strongest existing equivalent"
    ],
    "REVIEWER_CHECKLIST.md": [
        "Coherence",
        "Novelty / Redundancy",
        "Formula Stress Test",
        "Failure Cases",
        "Review Verdict"
    ],
    "REVIEW_QUESTIONS.md": [
        "Primary Question",
        "Counterexample Request",
        "Desired Review Style"
    ],
    "docs/OUTREACH_PLAN.md": [
        "controlled hostile review",
        "Do not lead with the largest philosophical claim.",
        "local correctness does not imply valid use"
    ],
    "docs/GITHUB_REVIEW_GUIDE.md": [
        "Severity Scale",
        "S5",
        "counterexamples"
    ]
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

    issue_templates = list(Path(".github/ISSUE_TEMPLATE").glob("*.md"))
    if len(issue_templates) < 5:
        raise SystemExit(f"Expected at least 5 issue templates, found {len(issue_templates)}")

    email_files = [
        Path("docs/OUTREACH_EMAIL_GENERAL.md"),
        Path("docs/OUTREACH_EMAIL_AI.md"),
        Path("docs/OUTREACH_EMAIL_MODEL_RISK.md"),
        Path("docs/OUTREACH_EMAIL_SYSTEMS.md"),
    ]

    for path in email_files:
        text = path.read_text(encoding="utf-8")
        if "Repository:" not in text:
            raise SystemExit(f"Email missing Repository line: {path}")
        if "hostile" not in text.lower():
            raise SystemExit(f"Email missing hostile-review framing: {path}")

    print("PASS outreach files")
    print("PASS required phrases")
    print("PASS issue templates")
    print("PASS email review framing")
    print("PASS overclaim discipline")
    print("All outreach-kit checks passed.")

if __name__ == "__main__":
    main()
