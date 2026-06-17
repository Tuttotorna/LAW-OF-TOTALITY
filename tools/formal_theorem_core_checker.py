from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md",
    "README.md",
    "FORMAL_SYSTEM.md",
    "ERROR_FORMULA.md",
    "REVIEW_FILE_MAP.md",
    "CLAIMS_FREEZE.md",
]

required_phrases = {
    "FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md": [
        "Formal Theorems and Counterexamples Core",
        "Every theory closes locally. Reality remains open.",
        "Structural error =",
        "local correctness does not imply valid use",
        "Incompleteness Alone Is Not Structural Error",
        "Wrong Game Condition",
        "Counterexample Class A",
        "Counterexample Class B",
        "Counterexample Class C",
        "Counterexample Class D",
        "Counterexample Class E",
        "Counterexample-ready by design.",
    ],
    "README.md": [
        "Formal Theorem and Counterexample Core",
        "FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md",
    ],
    "FORMAL_SYSTEM.md": [
        "Formal Theorem Companion",
        "Closed in theory. Open in reality.",
    ],
    "ERROR_FORMULA.md": [
        "Formal Error Core",
        "incompleteness alone is not error",
    ],
    "REVIEW_FILE_MAP.md": [
        "Formal Theorems and Counterexamples",
        "Are the counterexample classes strong enough",
    ],
    "CLAIMS_FREEZE.md": [
        "Post-v1 Clarification: Formal Theorem Core",
        "It does not change the validation status of the project.",
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

dangerous_patterns = [
    r"\bproves everything\b",
    r"\bsolves everything\b",
    r"\bvalidated theory of everything\b",
    r"\binfallible\b",
    r"\bcomplete explanation of reality\b",
    r"\bfinal theory\b",
]

safe_markers = [
    "avoid",
    "does not claim",
    "not claim",
    "forbidden",
    "do not claim",
    "negative example",
    "overclaim",
    "reject",
    "does not make",
    "doesn't make",
    "cannot make",
    "not validated",
    "not a validated",
    "not the final",
    "not final",
    "does not change the validation status",
]

violations = []

for md in ROOT.rglob("*.md"):
    rel = str(md.relative_to(ROOT))
    lines = md.read_text(encoding="utf-8", errors="ignore").splitlines()
    for idx, line in enumerate(lines, start=1):
        lower = line.lower()
        if any(marker in lower for marker in safe_markers):
            continue
        for pattern in dangerous_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append((rel, idx, pattern, line.strip()))

if violations:
    print("Overclaim violations found:")
    for rel, idx, pattern, line in violations:
        print(f"- {rel}:{idx}: {pattern} :: {line}")
    raise SystemExit("formal_theorem_core_checker.py FAIL")

print("formal_theorem_core_checker.py PASS")
