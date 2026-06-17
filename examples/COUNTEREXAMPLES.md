# Counterexamples

The Law of Totality must not diagnose every partial model as structurally wrong.

A partial framework is not automatically an error.

Structural error requires:

1. local closure;
2. use beyond valid scope;
3. excluded critical dependency.

If one of these is missing, the law does not diagnose structural error.

---

## Counterexample 1: Partial model used as partial model

### Case

A weather forecast states that it is reliable only within a limited time window and with probabilistic uncertainty.

The user treats it only as a local estimate.

### Audit

| Field | Answer |
|---|---|
| Object | Weather forecast |
| Framework | Probabilistic meteorological model |
| Actual use | General planning, not final certainty |
| Valid scope | Limited time window and probabilistic confidence |
| Local closure present? | no |
| Critical dependencies excluded? | not falsely hidden |
| Use beyond valid scope? | no |
| Structural error present? | no |

### Explanation

The forecast is partial, but it is not falsely closed.

No structural error occurs.

---

## Counterexample 2: Irrelevant excluded dependency

### Case

A model excludes a variable that has no effect on the actual use.

The missing dependency is not critical.

### Audit

| Field | Answer |
|---|---|
| Object | Model output |
| Framework | Local model |
| Actual use | Narrow decision |
| Valid scope | Declared narrow field |
| Local closure present? | possibly |
| Critical dependency excluded? | no |
| Use beyond valid scope? | no |
| Structural error present? | no |

### Explanation

Not every excluded dependency matters.

Only excluded critical dependencies generate structural error.

---

## Counterexample 3: Valid local closure

### Case

A mathematical operation is performed inside a fully specified formal system.

The result is used only inside that formal system.

### Audit

| Field | Answer |
|---|---|
| Object | Formal mathematical result |
| Framework | Fully specified formal system |
| Actual use | Internal formal derivation |
| Valid scope | The formal system itself |
| Local closure present? | yes |
| Critical dependency excluded? | no, relative to internal use |
| Use beyond valid scope? | no |
| Structural error present? | no |

### Explanation

The closure is local, declared and not abused beyond its scope.

No structural error occurs.

---

## Counterexample 4: Declared uncertainty

### Case

An AI answer states that it lacks current sources and that the answer is only a provisional hypothesis.

The user is not asked to treat it as final authority.

### Audit

| Field | Answer |
|---|---|
| Object | AI answer |
| Framework | Language model output |
| Actual use | Draft or provisional reasoning |
| Valid scope | Available context only |
| Local closure present? | no |
| Critical dependency excluded? | possibly, but declared |
| Use beyond valid scope? | no |
| Structural error present? | no |

### Explanation

The AI may be incomplete, but it is not falsely closed.

Structural error occurs only when the missing dependency is hidden while the answer is presented as sufficient.

---

## Final note

The Law of Totality is not a universal accusation against all models.

It is a diagnostic rule for false sufficiency.

A fragment is allowed to be a fragment.

It becomes structurally dangerous when it behaves as totality.
