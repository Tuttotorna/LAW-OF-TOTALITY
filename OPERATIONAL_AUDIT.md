# Operational Audit Protocol — v0.5.0

## 1. Goal

This protocol converts the Law of Totality into a practical audit.

It answers one question:

    Is this framework being used as sufficient for a use that requires something the framework excludes?

## 2. Required Inputs

Every audit must identify:

    x = object / manifestation / case under treatment
    F = framework / model / answer / procedure / theory / map
    U = intended concrete use
    A = answer / output / decision produced through F

If any of these is missing, the audit is incomplete.

## 3. Audit Sequence

### Step 1 — Identify x

    What is being treated?

Examples:

    a patient
    a legal case
    an AI answer
    a business decision
    a mathematical object
    a system failure
    a navigation route
    a model output

### Step 2 — Identify F

    What framework is being used to treat x?

Examples:

    statistical model
    legal category
    medical test
    financial model
    engineering simplification
    LLM response
    map
    metric
    policy
    algorithm

### Step 3 — Identify U

    What is the actual use?

The use must be concrete.

Weak:

    to understand the situation

Strong:

    to decide whether to approve the loan
    to choose medical treatment
    to deploy the model in production
    to navigate a mountain route in winter
    to classify a person as safe or unsafe

### Step 4 — Declare Valid Scope

    For which uses is F valid?

Output:

    ValidScope(F,x) = { declared valid uses }

If the valid scope is unknown, the framework cannot be treated as sufficient.

### Step 5 — Detect Local Closure

    Does F close x locally?

Examples:

    reduces x to a score
    reduces x to a legal category
    reduces x to a diagnosis
    reduces x to a map route
    reduces x to a probability
    reduces x to a short answer

If there is no local closure, this specific structural-error formula may not apply.

### Step 6 — List Critical Dependencies

    What must be preserved for U to be valid?

Examples:

    time
    context
    causality
    jurisdiction
    measurement uncertainty
    physical constraints
    social consequences
    distribution shift
    human override
    data provenance
    missing variables
    edge cases

Output:

    CriticalDepΩ(d,x,U)

### Step 7 — List Exclusions

    Which critical dependencies are excluded by F?

Output:

    ExcludedF(d)

### Step 8 — Apply Formula

Structural error exists if:

    LocalClosureF(x) = true
    ActualUseU(F,x) exceeds ValidScope(F,x) = true
    ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)] = true

Then:

    ErrΩ(x,F,U) = true

## 4. Severity

Severity increases with:

    1. irreversibility of U
    2. number of excluded critical dependencies
    3. consequence magnitude
    4. uncertainty level
    5. lack of human review
    6. inability to recover after deployment
    7. affected population size

Severity levels:

    LOW      = reversible, low consequence
    MEDIUM   = limited consequence, recoverable
    HIGH     = major consequence, hard to reverse
    CRITICAL = irreversible or systemic consequence

## 5. Correction

A correction must do at least one of these:

    1. reduce U until it fits ValidScope(F,x)
    2. expand F to preserve the missing dependency
    3. add another framework F2 that covers the excluded dependency
    4. block the decision
    5. mark the answer as insufficient
    6. require domain expert review

## 6. Audit Template

    Object x:
    Framework F:
    Actual use U:
    Output A:

    Local closure:
    Valid scope:
    Actual use within scope? yes/no

    Critical dependencies required by U:
    - d1
    - d2
    - d3

    Excluded by F:
    - d?

    Formula result:
    ErrΩ(x,F,U) = true/false

    Severity:
    Correction:
    Residual uncertainty:

## 7. Minimal Audit

If time is limited, use this compressed form:

    What is the use?
    What is the valid scope?
    What critical dependency required by the use is excluded?

If the third answer is non-empty and the use exceeds scope, the framework is structurally invalid for that use.
