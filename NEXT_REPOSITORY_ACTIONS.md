# Next Repository Actions

## Current status

The operational validation package has been added.

The repository now contains:

- validation protocol;
- comparative framework map;
- case studies;
- counterexample register;
- claim boundary;
- audit schema;
- audit engine;
- unit tests;
- cross-repo structural audit.

## Immediate technical correction

Generated Python files must not be committed.

This repository now excludes:

```text
__pycache__/
*.py[cod]
.pytest_cache/
.ipynb_checkpoints/
```

## Structural result of the first cross-repo audit

The first heuristic cross-repo audit identified three high-priority repositories:

```text
mathematics-beyond-human-habit
omnia-gsm8k-claim
reason-bridge
```

These repositories are not judged false by the audit.

They are structurally risky because their public framing may contain closure-heavy claims without enough scope-control language.

## Next validation step

The next step is not expansion.

The next step is correction.

For each high-priority repository, add:

```text
CLAIM_BOUNDARY.md
VALID_SCOPE.md
ASSUMPTIONS.md
FAILURE_MODES.md
```

Minimum correction:

```text
claim → valid scope → assumptions → excluded dependencies → validation status → failure modes
```

## Rule

No repository should publicly claim more than its validation level supports.

In Law of Totality terms:

```text
public claim must not exceed valid scope
```

Otherwise the repository itself becomes an example of the structural error it describes.
