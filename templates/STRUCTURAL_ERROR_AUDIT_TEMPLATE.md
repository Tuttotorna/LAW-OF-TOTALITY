# Structural Error Audit Template

## Object audited

| Field | Answer |
|---|---|
| Name of object | |
| Type of object | theory / model / AI answer / decision / project / protocol / forecast / safety claim / other |
| Domain | |
| Auditor | |
| Date | |
| Version or source | |

---

## 1. Object definition

### What is being judged?

Write the object clearly.

Do not audit a vague object.

| Question | Answer |
|---|---|
| What is the object? | |
| What claim, output, decision or action does it produce? | |
| What does it appear to close, decide, explain, predict or authorize? | |

---

## 2. Framework identification

### Which framework produces the judgment?

| Question | Answer |
|---|---|
| What framework is being used? | |
| What assumptions does it rely on? | |
| What does it include? | |
| What does it exclude? | |
| Is the framework formal, empirical, procedural, statistical, linguistic, institutional or mixed? | |

---

## 3. Actual use

### What is the output being used for?

This is the decisive field.

A framework can be valid for explanation but invalid for action.

A model can be valid for estimation but invalid for authorization.

An AI answer can be valid as a draft but invalid as final authority.

| Question | Answer |
|---|---|
| What is the actual use? | |
| Who or what relies on the output? | |
| Is the use theoretical, practical, operational, legal, financial, medical, safety-critical or public? | |
| What happens if the output is wrong or insufficient? | |

---

## 4. Valid scope

### Where is the framework legitimately usable?

| Question | Answer |
|---|---|
| What is the declared valid scope? | |
| What are the boundary conditions? | |
| What assumptions must remain true? | |
| What cases are outside scope? | |
| Is the actual use inside or outside this scope? | inside / outside / unclear |

---

## 5. Local closure check

### Does the framework locally close the object?

Local closure means that the framework presents the object as sufficiently explained, decided, predicted, authorized or completed.

| Question | Answer |
|---|---|
| Does the framework present a closed output? | yes / no / unclear |
| Is the output presented as complete, sufficient, final or decision-ready? | yes / no / unclear |
| Is uncertainty declared? | yes / no / unclear |
| Are missing dependencies declared? | yes / no / unclear |
| Closure verdict | local closure / open-provisional / unclear |

---

## 6. Dependency identification

### Candidate dependencies

List possible dependencies required by the actual use.

Do not classify everything as critical.

| Candidate dependency | Type | Why it may matter |
|---|---|---|
| | logical / formal / evidential / contextual / temporal / causal / operational / safety / human / resource / authority / interface | |
| | | |
| | | |

---

## 7. Dependency severity classification

Use the D0-D5 taxonomy.

| Level | Name | Meaning |
|---|---|---|
| D0 | Irrelevant | no effect on actual use |
| D1 | Background | present in the wider field but not decisive |
| D2 | Relevant | may influence the result |
| D3 | Material | can significantly affect the output |
| D4 | Critical | exclusion can invalidate the actual use |
| D5 | Blocking | use must not proceed without it |

### Classification table

| Dependency | Level | Reason for level | What would lower this level? |
|---|---|---|---|
| | D0 / D1 / D2 / D3 / D4 / D5 | | |
| | | | |
| | | | |

---

## 8. Excluded D4/D5 dependency check

Structural error requires an excluded D4 or D5 dependency.

| Question | Answer |
|---|---|
| Is there a D4 critical dependency? | yes / no / unclear |
| Is there a D5 blocking dependency? | yes / no / unclear |
| Which D4/D5 dependency is excluded? | |
| Is it included by the framework? | yes / no / unclear |
| Is it preserved by the framework? | yes / no / unclear |
| Is it declared as missing? | yes / no / unclear |
| Is it controlled by another mechanism? | yes / no / unclear |

---

## 9. Use-beyond-scope check

| Question | Answer |
|---|---|
| Is the actual use beyond the valid scope? | yes / no / unclear |
| Which scope boundary is exceeded? | |
| Is the scope violation declared? | yes / no / unclear |
| Is the output still being used as sufficient? | yes / no / unclear |

---

## 10. False sufficiency check

False sufficiency exists when a framework is treated as enough for an actual use while excluding a dependency required by that use.

| Question | Answer |
|---|---|
| Is the framework treated as sufficient? | yes / no / unclear |
| Is the missing dependency D4 or D5? | yes / no / unclear |
| Is the missing dependency required by the actual use? | yes / no / unclear |
| Is the missing dependency undeclared or uncontrolled? | yes / no / unclear |
| False sufficiency present? | yes / no / unclear |

---

## 11. Structural error verdict

The Law of Totality diagnoses structural error only if all four conditions are present:

1. local closure;
2. use beyond valid scope;
3. excluded D4/D5 dependency;
4. false sufficiency.

| Required condition | Present? | Evidence |
|---|---|---|
| Local closure | yes / no / unclear | |
| Use beyond valid scope | yes / no / unclear | |
| Excluded D4/D5 dependency | yes / no / unclear | |
| False sufficiency | yes / no / unclear | |

### Verdict

Select one:

- structural error;
- no structural error;
- insufficient evidence.

| Verdict | Answer |
|---|---|
| Final verdict | structural error / no structural error / insufficient evidence |
| Reason | |

---

## 12. Explanation

### If structural error is present

Use this form:

The framework may be locally valid, but it is structurally invalid for this actual use because it locally closes the object, is used beyond its valid scope, excludes a D4/D5 dependency required by the use, and is still treated as sufficient.

### If no structural error is present

Use this form:

The framework is partial, but it is not structurally erroneous under the Law of Totality because at least one required condition is absent.

### If evidence is insufficient

Use this form:

The audit cannot reach a structural error verdict because the actual use, valid scope, dependency level, exclusion mechanism or false sufficiency condition is not sufficiently established.

---

## 13. Falsification check

A diagnosis is weak if it cannot state what would defeat it.

| Question | Answer |
|---|---|
| What would prove that the dependency is not D4/D5? | |
| What would prove that the actual use is inside valid scope? | |
| What would prove that the framework includes or controls the dependency? | |
| What would prove that the framework was not treated as sufficient? | |
| What evidence is missing from this audit? | |

---

## 14. Correction path

If structural error is present, specify what must change.

| Correction type | Required action |
|---|---|
| Limit scope | |
| Declare missing dependency | |
| Include dependency | |
| Add evidence | |
| Add domain expert review | |
| Convert final answer into provisional answer | |
| Stop use until blocking dependency is resolved | |
| Other | |

---

## 15. Theory-to-reality bridge

Use this section when auditing a theory or model that wants to become operationally real.

| Field | Answer |
|---|---|
| Internal theoretical claim | |
| Declared scope | |
| Intended real use | |
| Dependencies required by that use | |
| Dependencies already included | |
| Dependencies missing | |
| Can the theory be used as sufficient now? | yes / no / unclear |
| What must be added before real use? | |

---

# Final audit summary

| Field | Answer |
|---|---|
| Object | |
| Framework | |
| Actual use | |
| Valid scope | |
| Main excluded dependency | |
| Dependency level | D0 / D1 / D2 / D3 / D4 / D5 |
| Local closure | yes / no / unclear |
| Use beyond scope | yes / no / unclear |
| False sufficiency | yes / no / unclear |
| Final verdict | structural error / no structural error / insufficient evidence |
| One-sentence conclusion | |
