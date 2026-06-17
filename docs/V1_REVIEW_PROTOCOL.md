# v1.0.0 Review Protocol

## Purpose

This protocol defines how external feedback should be handled.

## Step 1 — Convert Every Serious Criticism Into An Issue

Every substantive objection should become a GitHub issue.

Use labels:

    counterexample
    definition
    redundancy
    case-atlas
    use-case
    review

## Step 2 — Classify Severity

Severity scale:

    S1 minor wording or organization
    S2 definition unclear but fixable
    S3 serious claim or case weakness
    S4 critical formula failure on important class
    S5 fatal redundancy or non-operationality

## Step 3 — Map The Objection

For every objection, identify:

    x
    F
    U
    ValidScope
    d
    ExcludedF
    expected verdict
    reviewer verdict

If mapping is impossible, the objection may indicate a definition weakness.

## Step 4 — Decide Response Type

Possible responses:

    accept and revise;
    accept partially;
    reject with reason;
    defer pending domain expertise;
    convert to test case;
    narrow claim;
    remove case;
    harden definition.

## Step 5 — Prepare v1.1.0

The first post-review version should be:

    v1.1.0 Review Response Release

It should include:

    accepted objections;
    rejected objections;
    revised definitions;
    corrected cases;
    new negative controls;
    narrower claims if required;
    updated review status.

## Rule

No expansion before review response.

After v1.0.0, the project should not grow outward until it has absorbed external criticism.
