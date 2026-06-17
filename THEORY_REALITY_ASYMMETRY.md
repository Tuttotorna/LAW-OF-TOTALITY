# Theory-Reality Asymmetry

## Status

This document introduces a corollary of the Law of Totality.

It is not an independent totalizing claim.

It is an operational consequence of the core distinction between a finite framework and the real object it treats.

## Short Form

> Every theory closes locally. Reality remains open.
>
> Structural error begins when the closure is treated as the real.

Even shorter:

> Closed in theory. Open in reality.

## Core Statement

For every proper manifested object `x ≠ Ω`, any finite theory, model, map, rule, game, metric, proof environment, or framework `F` can only close `x` locally.

But the real object `x`, as manifested in `Ω`, remains structurally open with respect to the total field of dependencies.

Therefore:

```text
Closed_F(x) does not imply Closed_Ω(x)
```

For any proper real object:

```text
Manifest_Ω(x) ∧ x ≠ Ω ⇒ Open_Ω(x)
```

while any finite treatment requires some local closure:

```text
Theory_F(x) ⇒ LocalClosure_F(x)
```

The asymmetry is therefore:

```text
LocalClosure_F(x) ∧ Open_Ω(x)
```

## Meaning

A theory must close something in order to function.

It must select variables, define scope, stabilize language, choose assumptions, simplify dependencies, and make the object tractable.

This local closure is not an error.

It is the condition of finite understanding, calculation, decision, and action.

The error begins only when the local closure is treated as sufficient for an actual use that requires dependencies excluded by the framework.

## Relation to the Structural Error Formula

The Structural Error Formula is:

```text
Err_Ω(x,F,U) ⇔
LocalClosure_F(x)
∧ ActualUse_U(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDep_Ω(d,x,U) ∧ Excluded_F(d)]
```

The Theory-Reality Asymmetry explains why this formula is necessary:

```text
F closes locally.
x remains open in Ω.
U may require dependencies outside F.
```

The error is not closure itself.

The error is the false use of closure.

## Compact Error Form

```text
Structural error =
closed theory
+ open reality
+ actual use that treats the closure as sufficient
+ excluded critical dependency
```

## Non-Error Condition

A finite theory or model is not structurally invalid merely because it is incomplete.

It remains valid when:

```text
ActualUse_U(F,x) ⊆ ValidScope(F,x)
```

and when all dependencies critical for that use are preserved or explicitly accounted for:

```text
∀d [CriticalDep_Ω(d,x,U) → Preserved_F(d) ∨ ExplicitlyExcluded_F(d)]
```

The practical requirement is not omniscience.

The requirement is scope discipline.

## Examples

### Game Theory

A game closes a strategic situation into players, strategies, payoffs, information, and rules.

This closure may be valid for local analysis.

It becomes structurally invalid when an equilibrium inside the game is treated as sufficient for real-world strategy while excluding critical dependencies such as time, reputation, culture, coercion, institutions, asymmetric information, or future interaction.

```text
Equilibrium_G(x) ≠ ValidUse_Ω(G,x,U)
```

### Economic Metrics

A metric such as GDP, price, productivity, or profit locally closes a complex social field into a measurable quantity.

This closure may be useful for a defined use.

It becomes structurally invalid when the metric is used as a total proxy for welfare, stability, value, or social health while excluding critical dependencies such as distribution, ecological cost, unpaid labor, resilience, or long-term damage.

```text
Metric_F(x) ≠ TotalValue_Ω(x)
```

### Formal Proof

A formal proof closes a mathematical claim inside a formal environment.

This may be sufficient for certification inside that system.

It may not be sufficient for every use, such as explanation, transfer, intended-object alignment, theory-building, or scientific application, if those uses require dependencies not preserved by the formal encoding.

```text
FormalCorrectness_F(x) ≠ ValidUse_Ω(x,U)
```

### AI Answers

An AI answer locally closes a user request into a generated response.

This may be useful as a draft, summary, hypothesis, or local explanation.

It becomes structurally invalid when used as professional, legal, medical, technical, or factual authority while excluding critical dependencies such as source verification, currentness, jurisdiction, patient-specific data, domain expertise, or exact operating conditions.

```text
UsefulAnswer_F(x) ≠ ValidDecision_Ω(x,U)
```

## Philosophical Interpretation

The point is not that theories are useless because they are partial.

The point is that finite theories are useful precisely because they close.

But reality does not become closed because a theory has closed it.

The Law of Totality therefore closes the criterion without closing the real:

> It closes the criterion of structural error.
>
> It does not close reality itself.

## Public Formulation

Use this formulation externally:

> Every theory closes locally. Reality remains open.
> Structural error begins when the closure is treated as the real.

Avoid absolute overclaims that present the framework as a complete explanation of all reality, a final doctrine, or a closure of the infinite.

The precise claim is:

> A finite framework is valid only within the scope of the dependencies it preserves for the use being made of it.

## Review Challenge

To challenge this corollary, show one of the following:

1. a finite theory that treats a proper real object without local closure;
2. a proper real object `x ≠ Ω` that is fully closed in Ω;
3. a valid actual use `U` where excluded critical dependencies are required by the use but do not affect validity;
4. an existing framework that captures the same theory-reality asymmetry with equal or greater operational clarity.

Until then, the corollary remains a compact expression of the relation between finite theory and open reality.

## Relation to the Formal Theorem Core

The Theory-Reality Asymmetry is formalized further in:

[`FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md`](FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md)

The compact theorem schema is:

    Finite(F) and Treats(F,x) implies LocalClosure_F(x)

    Manifest_Ω(x) and Proper_Ω(x) implies Open_Ω(x)

Therefore:

    LocalClosure_F(x) and Open_Ω(x)

This is the formal basis of:

    Closed in theory. Open in reality.
