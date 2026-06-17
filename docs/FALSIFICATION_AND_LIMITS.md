# Falsification and Limits

## Purpose

The Law of Totality must not become a universal explanation that can absorb every possible outcome.

If the law can always say after the fact that a missing dependency caused the failure, then it is too broad.

This document defines:

1. when the Law of Totality should not be applied;
2. when the law fails as an audit;
3. what would weaken or falsify a specific diagnosis;
4. what remains outside the present theory;
5. how to prevent post-hoc misuse.

---

## Core operational claim

The Law of Totality diagnoses structural error only when all four conditions occur together:

1. a framework locally closes an object;
2. the framework is used beyond its valid scope;
3. a D4 critical or D5 blocking dependency required by the actual use is excluded;
4. the framework is still treated as sufficient.

In compact form:

> local closure + use beyond valid scope + excluded D4/D5 dependency + false sufficiency = structural error

If any of these conditions is absent, the Law of Totality should not diagnose structural error.

---

# 1. When the Law of Totality should not be applied

## 1.1 Partial model honestly used as partial

A framework may be incomplete but correctly limited.

If its incompleteness is declared and the framework is not treated as sufficient beyond its valid scope, there is no structural error.

### Verdict

No structural error.

Partiality alone is not error.

---

## 1.2 Formal result used only inside its formal system

A result proven inside a formal system may be valid within that system.

If it is used only inside that formal system, the Law of Totality does not diagnose structural error merely because the formal system is partial relative to reality.

### Verdict

No structural error.

Declared local closure is allowed.

---

## 1.3 Missing dependency is irrelevant

A missing factor is not critical merely because it exists.

If the missing factor does not affect the actual use, it cannot ground a structural error diagnosis.

### Verdict

No structural error.

The dependency is D0 or D1.

---

## 1.4 Missing dependency is already declared

A framework may explicitly say:

> this dependency is not included.

If the user does not treat the framework as sufficient beyond that declaration, there is no false sufficiency.

### Verdict

No structural error.

There may be limitation, but not structural misuse.

---

## 1.5 Use remains inside valid scope

A framework can be locally valid for a bounded use.

If the actual use does not exceed the valid scope, the Law of Totality should not diagnose structural error.

### Verdict

No structural error.

The model is being used correctly.

---

# 2. When a Law of Totality diagnosis fails

A specific diagnosis fails when it cannot establish at least one required condition.

## 2.1 No local closure

If the framework does not present the object as closed, complete, final, sufficient or decision-ready, the first condition is absent.

### Failed diagnosis

No structural error under the Law of Totality.

---

## 2.2 No use beyond valid scope

If the framework is used only inside its declared scope, the second condition is absent.

### Failed diagnosis

No structural error.

---

## 2.3 No D4/D5 dependency

If the missing dependency is only D0, D1, D2 or sometimes D3, the diagnosis is too strong.

### Failed diagnosis

The law may detect limitation or material uncertainty, but not structural error.

---

## 2.4 Dependency is included or controlled

If the framework already includes, preserves, controls or declares the dependency, the exclusion condition is absent.

### Failed diagnosis

No structural error from that dependency.

---

## 2.5 No false sufficiency

If the framework explicitly refuses final closure and is not used as sufficient, there is no false sufficiency.

### Failed diagnosis

No structural error.

---

# 3. What would falsify or weaken a specific diagnosis

The Law of Totality should not be judged only as a general idea.

Each application must be testable.

A specific diagnosis is weakened or falsified if one can show that:

1. the supposed critical dependency was not required by the actual use;
2. the dependency was already included by the framework;
3. the framework was not used beyond its valid scope;
4. the framework was not treated as sufficient;
5. the dependency could not materially affect the output, decision or action;
6. the same failure occurred even after the dependency was included;
7. the diagnosis was created only after the failure with no pre-identifiable dependency path;
8. the alleged missing dependency is vague and cannot be connected to a validity impact.

---

# 4. Anti-post-hoc discipline

The weakest misuse of the Law of Totality is:

> failure happened, therefore some critical dependency must have been excluded.

This is not acceptable.

The correct form is:

> before or during use, identify the dependency, classify it, show why the actual use requires it, and show how exclusion can invalidate the result.

A valid audit must specify:

1. the actual use;
2. the framework;
3. the valid scope;
4. the candidate dependency;
5. the dependency level;
6. the exclusion mechanism;
7. the false sufficiency claim;
8. the predicted validity impact.

Without this, the diagnosis remains speculative.

---

# 5. Limits of the Law of Totality

## 5.1 It is not a replacement for domain expertise

The law can identify the structure of a possible error.

It cannot replace medicine, law, engineering, finance, safety science, AI evaluation or any other domain practice.

It tells the auditor where to look.

It does not automatically provide the domain answer.

---

## 5.2 It does not prove which dependency is critical

The law requires classification.

It does not magically determine the classification.

Human or technical judgment is still required to decide whether a dependency is D0, D1, D2, D3, D4 or D5.

---

## 5.3 It does not eliminate uncertainty

The law may reduce false sufficiency.

It does not remove uncertainty from reality.

Some dependencies may be unknown, hidden, emerging, probabilistic or impossible to observe before action.

---

## 5.4 It is not a full causal theory

The law can identify missing causal dependencies when relevant.

But it does not itself provide a complete causal model of the domain.

---

## 5.5 It is not a full mathematical proof of totality

The repository proposes a structural criterion.

It does not prove absolute totality in a complete metaphysical or mathematical sense.

The operational version should remain focused:

> local closure + use beyond valid scope + excluded D4/D5 dependency + false sufficiency.

---

## 5.6 It is not automatically original

Existing frameworks already discuss model limitations, valid scope, assumptions, dependency management, safety cases and risk.

The Law of Totality must earn novelty by showing that its formula adds clarity, compression, transferability or earlier detection.

---

## 5.7 It does not make every theory wrong

A theory is not wrong because it is incomplete.

A theory becomes structurally wrong only when its incompleteness is treated as sufficient completeness for an actual use requiring excluded dependencies.

---

# 6. Negative cases required

Any serious application of the Law of Totality must include negative cases.

The law must be able to say:

> no structural error.

Examples:

- partial model declared as partial;
- missing dependency irrelevant to use;
- formal result used formally;
- output marked provisional;
- framework used inside valid scope;
- dependency included by the framework;
- no actual decision or real use depends on the output.

If the law cannot produce negative results, it is too broad.

---

# 7. Falsification table

| Required condition | What must be shown | What would defeat the diagnosis |
|---|---|---|
| Local closure | Framework presents output as sufficient, complete or decision-ready | Framework is explicitly provisional or open |
| Use beyond valid scope | Actual use exceeds declared scope | Use remains inside declared scope |
| D4/D5 dependency | Missing dependency is required by actual use | Dependency is irrelevant, background or merely optional |
| Exclusion | Framework does not include, preserve, control or declare dependency | Dependency is included or declared |
| False sufficiency | Framework is still treated as enough | Framework refuses final authority |

---

# 8. Strong version versus weak version

## Weak version

After a failure, identify a missing dependency and explain the failure.

This is weak because it can become post-hoc.

## Strong version

Before real use, identify D4/D5 dependencies that must not be excluded.

This is stronger because it can prevent structural error.

The mature Law of Totality should aim for the strong version.

---

# 9. Practical falsification protocol

For every audit, write:

| Field | Answer |
|---|---|
| Object | |
| Framework | |
| Actual use | |
| Valid scope | |
| Claimed local closure | |
| Candidate missing dependency | |
| Dependency level | D0 / D1 / D2 / D3 / D4 / D5 |
| Why actual use requires it | |
| How the framework excludes it | |
| How exclusion affects validity | |
| Was false sufficiency present? | yes / no |
| What would prove this diagnosis wrong? | |
| Verdict | structural error / no structural error / insufficient evidence |

---

# 10. Insufficient evidence verdict

The audit must allow a third verdict:

> insufficient evidence.

Not every case should be forced into yes or no.

Use insufficient evidence when:

- the actual use is unclear;
- the framework scope is unclear;
- the dependency level cannot be classified;
- the exclusion mechanism is unknown;
- the validity impact cannot be shown;
- the diagnosis is only rhetorical.

This protects the law from overclaiming.

---

## Template requirement

Real applications should use the audit template:

[`../templates/STRUCTURAL_ERROR_AUDIT_TEMPLATE.md`](../templates/STRUCTURAL_ERROR_AUDIT_TEMPLATE.md)

A diagnosis should not be considered mature until the template can be filled with:

- actual use;
- valid scope;
- D4/D5 dependency;
- exclusion mechanism;
- false sufficiency condition;
- falsification condition;
- final verdict.

If these fields cannot be completed, the correct verdict is usually:

> insufficient evidence.

# Final thesis

The Law of Totality becomes stronger when it defines where it stops.

It should not explain everything.

It should diagnose one specific error form:

> a local closure used as sufficient beyond its valid scope while excluding a D4/D5 dependency required by the actual use.

Everything outside that structure is not automatically a Law of Totality error.

A theory becomes serious not when it claims universal reach, but when it defines its limits without destroying its core.
