# Decision Validity — v0.5.0

## 1. Purpose

A decision can be locally rational and structurally invalid.

The question is not only:

    Was the decision justified inside the chosen framework?

The stronger question is:

    Was the chosen framework sufficient for the actual consequences of the decision?

## 2. Decision Formula

Let:

    D = decision
    F = decision framework
    x = object or situation decided upon
    U = practical deployment of the decision

Then:

    ValidDecisionΩ(D,F,x,U) ⇔
    JustifiedF(D,x)
    ∧ ActualUseU(D) ⊆ ValidScope(F,x)
    ∧ ∀d [CriticalDepΩ(d,x,U) ⇒ PreservedF(d)]

## 3. Decision Error

    DecisionErrΩ(D,F,x,U) ⇔
    JustifiedF(D,x)
    ∧ ActualUseU(D) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

## 4. Interpretation

The dangerous decision is not always irrational.

Often it is rational inside a narrow field and invalid in the wider field where consequences occur.

## 5. Examples

    cost-only decision excluding safety
    speed-only decision excluding maintenance
    legal-only decision excluding operational feasibility
    technical-only decision excluding human use
    AI-output decision excluding source uncertainty

## 6. Prevention

Before acting:

    1. identify the framework that justifies the decision
    2. identify the real-world deployment field
    3. identify dependencies required by deployment
    4. check which dependencies are excluded by the framework
    5. block, reduce, or redesign the decision

## 7. Core Sentence

> A decision is not valid because it is justified inside a framework; it is valid only if the framework is sufficient for the field where the decision acts.
