# Release Notes — v1.0.0

## Law of Totality v1.0.0 — External Review Release

This is the first external review release of the Law of Totality repository.

The release freezes the public claims and prepares the project for hostile review.

## Central Claim

    local correctness does not imply valid use.

## Core Formula

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

## Plain Meaning

A locally correct framework, model, rule, answer, metric, map, label, or theory becomes structurally invalid when it is used beyond its valid scope while excluding a dependency critical to the actual use.

## Current Status

    pre-review framework;
    externally readable;
    review-ready;
    not externally validated.

## Included Layers

### v0.5.0

Hardened formal and operational framework.

### v0.6.0

Error Atlas with 45 cases across 40 domains, including negative controls.

### v0.7.0

Hard comparative analysis against neighboring frameworks.

### v0.8.0

Short external paper.

### v0.9.0

Outreach kit, reviewer checklist, review questions, and GitHub issue templates.

### v1.0.0

Claim freeze and external review release.

## What Is New In v1.0.0

Added:

    CLAIMS_FREEZE.md
    EXTERNAL_REVIEW_RELEASE.md
    RELEASE_NOTES_v1.0.0.md
    REVIEW_FILE_MAP.md
    docs/FIRST_REVIEWER_SUBMISSIONS.md
    docs/V1_PUBLIC_STATEMENT.md
    docs/V1_REVIEW_PROTOCOL.md
    tools/release_checker.py

## What v1.0.0 Is For

This version is for:

    hostile review;
    expert criticism;
    counterexamples;
    redundancy checks;
    definition hardening;
    operational testing.

## What v1.0.0 Is Not For

This version is not for broad public promotion.

It is not a validation claim.

It is not a final theoretical closure.

## Recommended Review Path

1. Read `PAPER_SHORT.md`.
2. Read `TECHNICAL_SUMMARY.md`.
3. Read `CLAIMS_FREEZE.md`.
4. Review `ERROR_FORMULA.md`.
5. Test cases in `ERROR_ATLAS.md`.
6. Compare with `COMPARATIVE_ANALYSIS.md`.
7. Use `REVIEWER_CHECKLIST.md`.
8. Open issues using the templates.

## GitHub Review Infrastructure

The repository includes issue templates for:

    counterexamples;
    definition weaknesses;
    existing-framework equivalence;
    Case Atlas objections;
    operational use cases.

## Release Verdict

This is the version to attack.
