# Critical Dependency Taxonomy

## Purpose

The Law of Totality depends on the concept of critical dependency.

Without a rigorous definition, the formula risks becoming too elastic.

If every missing factor can be called a critical dependency after failure, the law becomes a post-hoc explanation rather than an operational audit.

This document defines a taxonomy for dependencies and a rule for when a dependency may be called critical.

---

## Core definition

A dependency is any condition, relation, constraint, assumption, context, input, boundary, evidence, interaction or external factor that can affect the validity of a framework for an actual use.

A critical dependency is a dependency whose exclusion can invalidate the actual use of a framework.

In compact form:

> A dependency is critical when the intended use cannot remain valid without it.

---

## Three-part test

A dependency may be classified as critical only if all three conditions are satisfied:

1. **Use relevance**  
   The dependency is required by the actual use, not merely by abstract completeness.

2. **Validity impact**  
   Excluding the dependency can change the correctness, safety, legitimacy, reliability or applicability of the output.

3. **Framework exclusion**  
   The dependency is not contained, preserved, declared or controlled by the framework being used.

If one of these conditions is absent, the dependency should not be classified as critical.

---

## Dependency levels

| Level | Name | Definition | Structural effect |
|---|---|---|---|
| D0 | Irrelevant dependency | A missing factor with no material effect on the actual use | No structural error |
| D1 | Background dependency | A contextual factor that exists but does not affect the present validity claim | No structural error |
| D2 | Relevant dependency | A factor that may influence the result but does not necessarily invalidate the use | Requires note or monitoring |
| D3 | Material dependency | A factor that can significantly affect the output or decision | Requires explicit treatment |
| D4 | Critical dependency | A factor whose exclusion can invalidate the actual use | Structural error if excluded and framework is treated as sufficient |
| D5 | Blocking dependency | A factor without which the actual use must not proceed | Immediate stop condition |

---

## Critical dependency threshold

A dependency reaches critical level when at least one of the following is true:

1. its absence can reverse the decision;
2. its absence can make the output unsafe;
3. its absence can make the output legally invalid;
4. its absence can make the output factually unsupported;
5. its absence can make the output inapplicable to the target case;
6. its absence can make the output operationally impossible;
7. its absence can make the output materially misleading;
8. its absence can produce hidden fragility under real use.

---

## Blocking dependency

A blocking dependency is stronger than a critical dependency.

A blocking dependency is a condition that must be resolved before the framework can be used at all for the intended action.

Examples:

- missing patient identity in a medical decision;
- missing jurisdiction in legal advice;
- missing structural load condition in safety-critical engineering;
- missing permission or authorization in public execution;
- missing source access for a factual claim presented as verified;
- missing safety protocol in a dangerous operation.

A blocking dependency does not merely weaken the output.

It prevents valid use.

---

# Dependency types

## 1. Logical dependency

A condition required for the internal coherence of a claim, proof, inference or argument.

### Examples

- a definition must be fixed;
- an inference rule must be valid;
- a premise must be available;
- a contradiction must be resolved.

### Critical when

The conclusion cannot follow without it.

---

## 2. Formal-system dependency

A condition required by a formal system, mathematical structure, notation, axiom set or rule system.

### Examples

- domain definition;
- axiom choice;
- boundary condition;
- variable constraint;
- permitted operation.

### Critical when

The result is used as if it held outside the formal system or outside the declared domain.

---

## 3. Evidential dependency

A source, observation, measurement, document, dataset or proof required to support a claim.

### Examples

- current source;
- full document;
- experimental evidence;
- dataset provenance;
- cited legal text;
- medical record;
- financial statement.

### Critical when

The claim is presented as verified, factual or decision-ready without the evidence required for that use.

---

## 4. Contextual dependency

A condition related to the surrounding situation in which the framework is applied.

### Examples

- jurisdiction;
- local regulation;
- user situation;
- physical environment;
- cultural context;
- organizational context;
- market condition.

### Critical when

The same output would be valid in one context but invalid in another.

---

## 5. Temporal dependency

A condition related to time, date, sequence, freshness, deadline, duration or timing.

### Examples

- current law;
- current price;
- updated weather;
- expiry date;
- maintenance interval;
- release version;
- project deadline.

### Critical when

Outdated or mistimed information can invalidate the use.

---

## 6. Causal dependency

A condition required for explaining, predicting or controlling an outcome.

### Examples

- mechanism;
- trigger condition;
- failure cause;
- interaction between variables;
- environmental effect;
- biological pathway;
- mechanical force.

### Critical when

The framework claims prediction or control while excluding a causal factor that can change the outcome.

---

## 7. Operational dependency

A condition required to execute a plan, project, protocol or action.

### Examples

- confirmed roles;
- logistics;
- equipment;
- budget;
- transport;
- permissions;
- backup plans;
- communication chain;
- decision authority.

### Critical when

The plan is treated as execution-ready without the conditions needed for execution.

---

## 8. Safety dependency

A condition required to prevent harm, failure, injury, collapse or unacceptable risk.

### Examples

- medical supervision;
- emergency protocol;
- load tolerance;
- protective equipment;
- weather window;
- redundancy;
- evacuation plan;
- risk threshold.

### Critical when

The actual use can cause harm if the dependency is absent.

Safety dependencies often become blocking dependencies.

---

## 9. Human-behavior dependency

A condition related to how people actually behave rather than how the model assumes they behave.

### Examples

- compliance;
- fatigue;
- misunderstanding;
- incentives;
- coordination;
- panic;
- negligence;
- overconfidence;
- communication failure.

### Critical when

The framework assumes ideal human behavior but the actual use depends on non-ideal human behavior.

---

## 10. Resource dependency

A condition related to available resources.

### Examples

- money;
- time;
- labor;
- expertise;
- energy;
- materials;
- computing capacity;
- maintenance capacity.

### Critical when

The intended use cannot be completed or sustained without the resource.

---

## 11. Authority dependency

A condition related to permission, legitimacy, responsibility or right to decide.

### Examples

- legal authorization;
- institutional approval;
- professional license;
- medical authority;
- command structure;
- signed confirmation;
- stakeholder mandate.

### Critical when

The action cannot be validly performed without proper authority.

---

## 12. Interface dependency

A condition related to interaction between systems, people, components, organizations or frameworks.

### Examples

- API compatibility;
- equipment connection;
- team coordination;
- handoff procedure;
- data format;
- organizational interface;
- physical interface.

### Critical when

The failure occurs at the boundary between parts, even if each part is locally valid.

---

# Classification procedure

To classify a dependency, use this sequence.

## Step 1 — Define the actual use

Do not classify dependencies in the abstract.

A dependency is critical only relative to an actual use.

Question:

> What is this framework being used to decide, predict, justify, execute or authorize?

---

## Step 2 — Define the valid scope

Question:

> Where is this framework legitimately valid?

If the use remains inside the valid scope, no structural error follows merely from incompleteness.

---

## Step 3 — List candidate dependencies

List every dependency that may affect the actual use.

Do not classify yet.

At this stage, collect candidates.

---

## Step 4 — Remove irrelevant dependencies

A missing factor is not critical merely because it exists.

Remove dependencies that do not affect the actual use.

---

## Step 5 — Classify severity

Assign each dependency a level:

- D0 irrelevant;
- D1 background;
- D2 relevant;
- D3 material;
- D4 critical;
- D5 blocking.

---

## Step 6 — Test exclusion

A critical dependency matters for the Law of Totality only if the framework excludes it, hides it, ignores it or fails to preserve it.

If the framework includes, declares or controls the dependency, no structural error follows from that dependency.

---

## Step 7 — Test false sufficiency

Structural error occurs only if the framework is still treated as sufficient despite excluding the critical dependency.

If the framework declares the missing dependency and refuses final closure, no structural error occurs.

---

# Anti-post-hoc rule

A dependency cannot be classified as critical merely because a failure occurred.

The audit must specify:

1. what the dependency was;
2. what actual use required it;
3. why the framework did not include it;
4. how its exclusion could invalidate the use;
5. whether this could have been identified before the failure.

If these five points cannot be stated, the diagnosis remains weak.

---

# Pre-declaration rule

For serious use, critical dependencies should be identified before action when possible.

The stronger form of the law is not:

> after failure, find what was missing.

The stronger form is:

> before use, identify what must not be missing.

This turns the Law of Totality from diagnosis into prevention.

---

# Negative test

The law must be able to say:

> this dependency is not critical.

A dependency is not critical when:

- it does not affect the actual use;
- it is already included by the framework;
- it is declared as missing and the framework is not treated as sufficient;
- it belongs to a different use;
- it changes detail but not validity;
- it is speculative and unsupported;
- it cannot be connected to a concrete validity impact.

---

# Audit table

| Field | Answer |
|---|---|
| Framework | |
| Actual use | |
| Valid scope | |
| Candidate dependency | |
| Dependency type | logical / formal / evidential / contextual / temporal / causal / operational / safety / human / resource / authority / interface |
| Dependency level | D0 / D1 / D2 / D3 / D4 / D5 |
| Why this use requires it | |
| What happens if excluded | |
| Is it included by the framework? | yes / no |
| Is it declared as missing? | yes / no |
| Is the framework still treated as sufficient? | yes / no |
| Structural verdict | no error / monitor / material gap / structural error / stop condition |

---

# Verdict language

## D0 — Irrelevant

The dependency does not affect the actual use. Its exclusion does not create structural error.

## D1 — Background

The dependency exists in the wider field but does not materially affect the present validity claim.

## D2 — Relevant

The dependency may influence the result and should be noted or monitored, but its exclusion does not yet invalidate the use.

## D3 — Material

The dependency can significantly affect the output. The framework requires correction, qualification or additional evidence.

## D4 — Critical

The dependency is required for the actual use. If excluded while the framework is treated as sufficient, structural error is present.

## D5 — Blocking

The dependency is required before the use can proceed. If missing, the action must stop or remain provisional.

---

# Relation to the Law of Totality

The Law of Totality is not triggered by every missing dependency.

It is triggered by excluded critical dependencies under false sufficiency.

The complete operational form is:

> structural error occurs when a framework locally closes an object, is used beyond its valid scope, and excludes a D4 or D5 dependency required by the actual use, while still being treated as sufficient.

---

# Final thesis

A dependency is not critical because it is missing.

A dependency is critical because the actual use cannot remain valid without it.

The main discipline of the Law of Totality is therefore not to multiply missing factors.

It is to identify the few missing factors that determine whether local validity can become real-world validity.
