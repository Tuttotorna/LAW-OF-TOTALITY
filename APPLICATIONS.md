# Applications — v0.5.0

## 1. AI Answers

Problem:

    An AI answer may be correct inside its available context but invalid for the user's intended use.

Audit:

    x = user's question
    F = model context / retrieved sources / reasoning frame
    U = user's intended action
    d = missing source, date, jurisdiction, domain constraint, measurement, safety factor

Correction:

    answer with scope
    retrieve missing dependency
    block high-stakes closure

## 2. Model Risk

Problem:

    A model trained and validated under one distribution is used under another.

Audit:

    x = modeled phenomenon
    F = model
    U = deployment environment
    d = distribution shift, data drift, population change, feedback loop

Correction:

    monitor drift
    restrict deployment
    revalidate
    add fallback controls

## 3. Medicine

Problem:

    A test result is treated as a complete diagnosis.

Audit:

    x = patient
    F = single test
    U = treatment decision
    d = symptoms, history, contraindications, differential diagnosis, comorbidities

Correction:

    restore clinical context
    require physician review
    avoid single-indicator closure

## 4. Law

Problem:

    A generic legal explanation is used as binding legal advice.

Audit:

    x = legal situation
    F = generic legal information
    U = procedural/legal action
    d = jurisdiction, documents, dates, exceptions, licensed interpretation

Correction:

    reduce answer to general information
    require jurisdiction-specific review

## 5. Engineering

Problem:

    A simplified calculation is used for real deployment outside assumptions.

Audit:

    x = physical system
    F = simplified model
    U = deployment
    d = tolerances, fatigue, temperature, loads, material defects, edge cases

Correction:

    validate assumptions
    run stress tests
    add safety factors

## 6. Business

Problem:

    A metric becomes the decision.

Audit:

    x = business system
    F = KPI
    U = strategic decision
    d = customer trust, long-term risk, incentives, hidden costs, regulatory exposure

Correction:

    restore multi-metric review
    include consequence analysis

## 7. Personal Decisions

Problem:

    A person decides from one emotional, financial, or social fragment.

Audit:

    x = life situation
    F = narrow perspective
    U = irreversible decision
    d = time, consequences, health, relationships, resources, future constraints

Correction:

    delay irreversible action
    expand dependency map
    ask domain-specific support

## 8. Mathematics

Problem:

    A representation is treated as the object itself.

Audit:

    x = mathematical object
    F = representation / base / notation / transformation
    U = claim about the object as such
    d = invariance, representation-dependence, hidden assumptions

Correction:

    compare across representations
    declare representational scope
    avoid projecting local artifacts onto the object

## 9. Universal Application Pattern

    Find the local closure.
    Find the actual use.
    Find the valid scope.
    Find the excluded critical dependency.

If all four are present, the structural error is present.
