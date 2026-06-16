# Related Work — v0.5.0

## 1. Purpose

This file prevents false novelty.

The Law of Totality is not presented as disconnected from existing fields. Its potential novelty is the compressed formula:

    local closure + use beyond scope + excluded critical dependency

## 2. Model Risk Management

Model risk management already recognizes that models have limits, assumptions, validation requirements, governance requirements, and use constraints.

Overlap:

    ValidScope(F,x)
    ActualUseU(F,x)
    model limitations
    model validation
    use monitoring

Difference:

    Law of Totality expresses the failure pattern as a general structural formula not limited to financial models.

Relevant reference:

    Federal Reserve / OCC model risk management guidance.

## 3. NIST AI Risk Management Framework

The NIST AI Risk Management Framework addresses AI risks through mapping, measuring, managing, and governing AI systems.

Overlap:

    context of use
    risk identification
    trustworthiness
    governance
    deployment constraints

Difference:

    Law of Totality focuses specifically on the structural error created when an AI answer or model output is used as sufficient beyond its valid scope.

## 4. STAMP / STPA Systems Safety

STAMP/STPA shifts attention from component failure to system-level constraints, unsafe control actions, feedback, and sociotechnical interactions.

Overlap:

    system context
    control limits
    unsafe use
    missing constraints
    failure beyond component correctness

Difference:

    Law of Totality generalizes the same type of error beyond safety engineering into any framework-use relation.

## 5. Epistemology and Philosophy of Science

Many traditions already distinguish:

    map vs territory
    model vs reality
    abstraction vs object
    contextual validity
    limits of representation

Overlap:

    finite representation cannot exhaust the object

Difference:

    Law of Totality gives an operational audit formula for when finite representation becomes structurally invalid in use.

## 6. Systems Thinking

Systems thinking emphasizes interdependence, feedback, emergence, context, and non-isolation.

Overlap:

    objects cannot be fully understood as isolated fragments

Difference:

    Law of Totality isolates a specific error signature:
    a local closure treated as sufficient under excluded critical dependency.

## 7. Potential Novel Contribution

The candidate contribution is not the generic observation that context matters.

The candidate contribution is this compression:

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

This turns a broad intuition into a repeatable diagnostic structure.

## 8. Required Future Work

To establish stronger novelty, the repository must add:

    1. comparison table against model risk management
    2. comparison table against NIST AI RMF
    3. comparison table against STAMP/STPA
    4. applied case studies
    5. adversarial tests
    6. external review
    7. domain-specific validation

## 9. Review-Resistant Novelty Sentence

> The repository does not claim that scope, context, or dependency are new. It claims that a recurring structural error can be compressed into a single operational formula connecting local closure, actual use, valid scope, and excluded critical dependency.
