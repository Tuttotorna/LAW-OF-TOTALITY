# Example Audit: AI Hallucination

## Case

An AI system gives a confident answer to a user.

The answer is grammatically coherent, plausible and presented as complete.

However, the AI lacks access to a critical dependency required for the actual use.

Examples:

- current law;
- full document context;
- patient-specific data;
- real-time facts;
- financial constraints;
- private contractual details;
- jurisdiction;
- source verification.

---

## Audit table

| Field | Answer |
|---|---|
| Object | AI-generated answer |
| Framework | Language model output based on available context/training/retrieval |
| Actual use | User may rely on the answer as sufficient for decision or action |
| Valid scope | Drafting, explanation, hypothesis, bounded answer from available evidence |
| Local closure present? | yes, if the answer is presented as complete |
| Critical dependencies for this use | current facts, source grounding, complete context, domain-specific constraints |
| Excluded critical dependencies | depends on case: missing source, missing current data, missing jurisdiction, missing document, missing patient-specific facts |
| Use beyond valid scope? | yes, if the answer is treated as final authority despite missing dependencies |
| Structural error present? | yes |
| Explanation | The hallucination is not only a false sentence. It is a false closure: the system presents a locally generated answer as sufficient while excluding dependencies required by the actual use. |

---

## Structural diagnosis

The AI does not fail only because it produces an incorrect phrase.

It fails structurally when it closes the answer beyond the evidence field available to it.

The structural error is:

> fluent closure without sufficient dependency relation.

---

## Corrective rule

Before output, the AI should identify:

1. object of the answer;
2. framework used;
3. intended use;
4. valid scope;
5. critical dependencies included;
6. critical dependencies missing.

If a critical dependency is missing, the AI must not present the answer as closed or sufficient.

---

## Minimal conclusion

AI hallucination is structurally interpretable as:

> local closure + use beyond valid scope + excluded critical dependency.
