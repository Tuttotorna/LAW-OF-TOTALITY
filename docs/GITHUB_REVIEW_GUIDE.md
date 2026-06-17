# GitHub Review Guide — v0.9.0

## Purpose

This guide explains how external reviewers should use GitHub issues.

## Issue Types

Use one of the templates:

    counterexample.md
    definition_weakness.md
    existing_framework_equivalent.md
    case_atlas_objection.md
    operational_use_case.md

## Best First Review

Open an issue titled:

    Strongest objection: [short description]

Then include:

    target file
    relevant formula component
    objection
    proposed correction
    severity

## Severity Scale

### S1 — Minor

Wording, clarity, typo, organization.

### S2 — Moderate

Definition unclear but fixable.

### S3 — Serious

Claim overextended or case weak.

### S4 — Critical

Formula fails on important class of cases.

### S5 — Fatal

Existing framework already covers the same structure with equal or greater clarity, or the formula is non-operational.

## Review Priority

Highest priority:

    counterexamples
    redundancy claims
    weak definitions
    misclassified cases
    scope errors

Lowest priority:

    stylistic preference
    general philosophical disagreement without specific case
    praise without objection
