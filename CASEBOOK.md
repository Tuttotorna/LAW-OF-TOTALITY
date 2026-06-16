# Casebook — v0.5.0

## Case 1 — Locally Correct, Structurally Invalid

    A weather app says: "No rain today."

Inside F:

    correct for the city forecast area

Actual use:

    decide whether to cross an exposed mountain ridge

Excluded dependencies:

    altitude
    microclimate
    wind exposure
    storm timing
    route duration

Result:

    ErrΩ(x,F,U) = true

## Case 2 — Locally Limited, Structurally Valid

    A weather app says: "No rain today in the city center."

Actual use:

    decide whether to carry an umbrella for a city walk

Result:

    ErrΩ(x,F,U) = false

Reason:

    The use remains inside valid scope.

## Case 3 — AI Legal Output

    F = general AI explanation
    U = file an actual legal motion

Critical dependencies:

    jurisdiction
    court rules
    deadlines
    documents
    licensed review

If excluded, the AI answer cannot be structurally valid for U.

## Case 4 — KPI Governance

    F = revenue metric
    U = decide company strategy

Excluded dependencies:

    customer retention
    legal risk
    employee burnout
    brand damage
    future liabilities

The decision may be locally rational and structurally invalid.

## Case 5 — No Structural Error

    F = rough estimate
    U = informal brainstorming

Excluded dependencies are not critical for the use.

Result:

    ErrΩ(x,F,U) = false

## Case 6 — Arithmetic Slip

    17 + 25 = 43

This is false, but not automatically a structural error under this framework.

It becomes structurally relevant only if the wrong result is used as sufficient for a consequential decision without verification.
