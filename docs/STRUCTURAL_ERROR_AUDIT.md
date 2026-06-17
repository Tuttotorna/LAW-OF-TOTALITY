# Structural Error Audit

## Purpose

This audit tests whether a framework, model, theory, answer, protocol or decision is being used beyond its valid scope while excluding a dependency required by the actual use.

The audit does not ask whether the framework is useful.

It asks whether the framework is being falsely treated as sufficient.

---

## Six audit questions

### 1. What is the object being judged?

Define the object.

Examples:

- an AI answer;
- a forecast;
- an engineering design;
- a medical decision;
- a legal interpretation;
- an investment model;
- a safety protocol.

---

### 2. Which framework is being used?

Identify the framework that produces the judgment.

Examples:

- a statistical model;
- a legal rule;
- a dataset;
- an engineering simulation;
- a medical guideline;
- a language model;
- a financial spreadsheet;
- a formal theory.

---

### 3. What is the actual use?

Define what the judgment is being used for in reality.

This is critical.

A framework may be valid for explanation but invalid for action.

A model may be valid for probability estimation but invalid for operational command.

An AI answer may be valid as a draft but invalid as final authority.

---

### 4. What is the valid scope of the framework?

Define where the framework is legitimately usable.

Examples:

- time range;
- jurisdiction;
- physical assumptions;
- population limits;
- dataset boundaries;
- environmental conditions;
- formal-system boundaries;
- intended use declared by the model.

---

### 5. Which dependencies are critical for the actual use?

List the dependencies required for the real use to be valid.

Examples:

- current facts;
- legal context;
- patient-specific data;
- environmental stress;
- material fatigue;
- human behavior;
- liquidity;
- regulation;
- maintenance;
- timing;
- hidden constraints;
- external system interactions.

---

### 6. Which critical dependencies are excluded?

Identify which required dependencies are absent from the framework.

This is the decisive point.

A missing dependency matters only if it is critical for the actual use.

---

## Verdict rule

Structural error is present when all three conditions hold:

1. the framework locally closes the object;
2. the framework is used beyond its valid scope;
3. a critical dependency required by the actual use is excluded.

If one of the three conditions is absent, the law does not diagnose structural error.

---

## Audit table

| Field | Answer |
|---|---|
| Object | |
| Framework | |
| Actual use | |
| Valid scope | |
| Local closure present? | yes / no |
| Critical dependencies for this use | |
| Excluded critical dependencies | |
| Use beyond valid scope? | yes / no |
| Structural error present? | yes / no |
| Explanation | |

---

## Minimal verdict language

### If structural error is present

The framework may be locally correct, but it is structurally invalid for this use because it excludes a dependency that is critical for the actual situation while being treated as sufficient.

### If structural error is absent

The framework is partial, but it is not being falsely treated as total or sufficient beyond its declared valid scope.

---

## Important limitation

The audit must not become a post-hoc excuse.

It is not enough to say after a failure:

> a dependency was missing.

The audit must identify:

1. which dependency was missing;
2. why it was critical;
3. why the actual use required it;
4. why the framework excluded it;
5. how this exclusion changed the validity of the decision.

Without this, the diagnosis is not yet operational.
