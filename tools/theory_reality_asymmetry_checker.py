from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "THEORY_REALITY_ASYMMETRY.md",
    "README.md",
    "FORMAL_SYSTEM.md",
    "ERROR_FORMULA.md",
    "GLOSSARY.md",
    "REVIEW_FILE_MAP.md",
]

required_phrases = {
    "THEORY_REALITY_ASYMMETRY.md": [
        "Every theory closes locally. Reality remains open.",
        "Closed in theory. Open in reality.",
        "Structural error begins when the closure is treated as the real.",
        "LocalClosure_F(x) ∧ Open_Ω(x)",
        "The error is not closure itself.",
        "The error is the false use of closure.",
    ],
    "README.md": [
        "Theory-Reality Asymmetry",
        "Every theory closes locally. Reality remains open.",
    ],
    "FORMAL_SYSTEM.md": [
        "Corollary: Theory-Reality Asymmetry",
        "Theory_F(x) ⇒ LocalClosure_F(x)",
    ],
    "ERROR_FORMULA.md": [
        "Theory-Reality Asymmetry and the Error Formula",
        "closed theory",
        "open reality",
        "excluded critical dependency",
    ],
    "GLOSSARY.md": [
        "Theory-Reality Asymmetry",
        "Local Closure",
        "Open Reality",
    ],
    "REVIEW_FILE_MAP.md": [
        "THEORY_REALITY_ASYMMETRY.md",
        "Does the corollary follow from the core formal system?",
    ],
}

for file in required_files:
    path = ROOT / file
    if not path.exists():
        raise SystemExit(f"Missing required file: {file}")

for file, phrases in required_phrases.items():
    text = (ROOT / file).read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise SystemExit(f"Missing phrase in {file}: {phrase}")

dangerous_absolute_patterns = [
    r"\bproves everything\b",
    r"\bsolves everything\b",
    r"\bvalidated theory of everything\b",
    r"\binfallible\b",
    r"\bcomplete explanation of reality\b",
]

def is_negated_or_safe(line: str) -> bool:
    lower = line.lower()

    safe_markers = [
        "avoid",
        "does not claim",
        "not claim",
        "forbidden",
        "do not claim",
        "not an",
        "not a",
        "reject",
        "overclaim",
        "negative example",
        "does not make",
        "doesn't make",
        "do not make",
        "not make",
        "cannot make",
        "does not become",
        "doesn't become",
        "not infallible",
        "is not infallible",
        "not validated",
        "not a validated",
        "not the final",
        "not final",
    ]

    return any(marker in lower for marker in safe_markers)

violations = []

for md in ROOT.rglob("*.md"):
    rel = str(md.relative_to(ROOT))
    lines = md.read_text(encoding="utf-8", errors="ignore").splitlines()
    for idx, line in enumerate(lines, start=1):
        if is_negated_or_safe(line):
            continue
        for pattern in dangerous_absolute_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append((rel, idx, pattern, line.strip()))

if violations:
    print("Overclaim violations found:")
    for rel, idx, pattern, line in violations:
        print(f"- {rel}:{idx}: {pattern} :: {line}")
    raise SystemExit("theory_reality_asymmetry_checker.py FAIL")

print("theory_reality_asymmetry_checker.py PASS")
