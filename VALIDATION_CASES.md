# Validation Cases — v0.5.0

## 1. Purpose

This file defines how the framework can be tested.

The framework becomes stronger only if it can identify:

    true positives
    true negatives
    false positives
    false negatives

## 2. Positive Case Structure

A valid positive case must show:

    1. x exists as the object under treatment.
    2. F locally closes x.
    3. U uses F beyond ValidScope(F,x).
    4. U requires at least one critical dependency d.
    5. F excludes d.
    6. The failure is explained by that exclusion.

## 3. Negative Case Structure

A valid negative case must show at least one of these:

    1. F does not locally close x.
    2. U remains inside ValidScope(F,x).
    3. No dependency excluded by F is critical for U.
    4. The failure is not caused by framework sufficiency.

## 4. Falsification Conditions

The framework is weakened if:

    1. it labels every error as structural without distinction;
    2. it cannot distinguish local error from structural error;
    3. it cannot identify the excluded dependency;
    4. it cannot identify the concrete use U;
    5. it treats every dependency as critical;
    6. it gives no correction path;
    7. it cannot produce true negative cases.

## 5. Case A — Map Used Outside Scale

    x = territory
    F = city tourist map
    U = mountain rescue navigation in winter
    LocalClosureF(x) = true
    ValidScope(F,x) = tourist navigation inside city
    CriticalDepΩ(d,x,U) = altitude, snow, trail condition, weather exposure
    ExcludedF(d) = true
    ErrΩ(x,F,U) = true

Why:

    The map may be locally correct for city tourism but structurally invalid for mountain rescue.

## 6. Case B — Medical Test Used As Full Diagnosis

    x = patient
    F = single lab value
    U = definitive treatment decision
    ValidScope(F,x) = partial clinical indicator
    CriticalDepΩ(d,x,U) = symptoms, history, differential diagnosis, contraindications
    ExcludedF(d) = true
    ErrΩ(x,F,U) = true

## 7. Case C — AI Answer Used As Legal Advice

    x = legal situation
    F = generic LLM answer
    U = binding legal action
    ValidScope(F,x) = general informational explanation
    CriticalDepΩ(d,x,U) = jurisdiction, dates, documents, procedural posture, licensed review
    ExcludedF(d) = true
    ErrΩ(x,F,U) = true

## 8. Case D — Correct Formula Used Outside Assumptions

    x = physical system
    F = simplified formula
    U = high-stakes engineering deployment
    ValidScope(F,x) = idealized conditions
    CriticalDepΩ(d,x,U) = friction, material fatigue, temperature, tolerances
    ExcludedF(d) = true
    ErrΩ(x,F,U) = true

## 9. Negative Case A — Map Used Correctly

    x = city center
    F = city tourist map
    U = find a museum inside the mapped area
    ActualUseU(F,x) ⊆ ValidScope(F,x)
    ErrΩ(x,F,U) = false

## 10. Negative Case B — Approximation Declared As Approximation

    x = early estimate
    F = rough model
    U = preliminary discussion only
    CriticalDepΩ(d,x,U) excluded but not critical for U
    ErrΩ(x,F,U) = false

## 11. Negative Case C — Arithmetic Slip

    x = calculation
    F = arithmetic
    U = compute 17+25
    failure = person writes 43 instead of 42
    ErrΩ(x,F,U) = false unless the wrong number is later treated as sufficient for a use requiring verification

## 12. Validation Table

| Case | Expected Result | Reason |
|---|---|---|
| Map outside scale | Error | Excluded critical field conditions |
| Medical test as diagnosis | Error | Partial indicator treated as sufficient |
| AI legal answer as binding advice | Error | Jurisdiction/documents/review excluded |
| Formula outside assumptions | Error | Assumption mismatch |
| Map inside scale | No error | Use remains inside scope |
| Rough estimate for discussion | No error | Excluded dependencies not critical for use |
| Arithmetic slip alone | No structural error | Not framework-sufficiency failure |
