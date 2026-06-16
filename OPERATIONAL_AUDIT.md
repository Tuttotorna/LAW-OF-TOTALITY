# Operational Audit Protocol

## Purpose

This file turns the Law of Absolute Non-Closure into an operational audit.

The law is not only:

~~~text
Everything depends.
~~~

The operational form is:

~~~text
A model fails structurally when it is used beyond its valid scope while excluding a critical determinability-condition.
~~~

---

## Audit Formula

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

---

## Required Inputs

For each audit, identify:

~~~text
x = manifestation, object, event, answer, decision, system
F = framework, model, theory, algorithm, discipline, answer
U = actual use or deployment
LC = local closure made by F
VS = valid scope of F
AU = actual use of F
D = candidate determinability-conditions
CD = critical determinability-conditions for U
EX = conditions excluded by F
FR = observed or expected fragility
CORR = corrected scope or corrected model
~~~

---

## Audit Steps

## Step 1 — Identify x

~~~text
What is being treated?
What is the manifestation under analysis?
Is x a thing, event, state, process, answer, model, decision, or system?
~~~

## Step 2 — Identify F

~~~text
What framework is being used?
What model, theory, algorithm, answer, discipline, or representation closes x locally?
~~~

## Step 3 — Identify Local Closure

~~~text
What does F treat as settled, complete, sufficient, calculable, classified, decided, or closed?
~~~

## Step 4 — Identify Valid Scope

~~~text
Inside which conditions is F valid?
What assumptions does F require?
What scale, context, data, axioms, environment, or use-case does F presuppose?
~~~

## Step 5 — Identify Actual Use

~~~text
How is F actually being used?
Is F being used beyond its declared or valid scope?
Is it being used as if it were sufficient for the real field?
~~~

## Step 6 — Identify Critical Conditions

~~~text
Which determinability-conditions are necessary for x in use U?
Which dependencies matter for this decision, failure, diagnosis, prediction, proof, or deployment?
~~~

## Step 7 — Check Exclusion

~~~text
Does F exclude any critical condition?
Does F suppress, ignore, abstract away, or hide a dependency required by U?
~~~

## Step 8 — Detect Structural Error

If all three hold:

~~~text
LocalClosureF(x)
ActualUseU(F,x) exceeds ValidScope(F,x)
ExcludedCriticalDepΩ(x,F,U) ≠ ∅
~~~

then:

~~~text
ErrΩ(x,F,U)
~~~

## Step 9 — Correct

Correction may require:

~~~text
declaring scope
restricting use
adding excluded dependencies
changing model
changing decision
changing data
changing representation
opening the field
~~~

---

## Minimal Audit Table

| Field | Fill |
|---|---|
| x | manifestation under analysis |
| F | model/framework used |
| U | actual use |
| LocalClosureF(x) | what F closes |
| ValidScope(F,x) | where F is valid |
| ActualUseU(F,x) | how F is used |
| CriticalDepΩ(d,x,U) | dependency required by use |
| ExcludedF(d) | dependency excluded by F |
| Error? | yes/no |
| Correction | scope, dependency, or model correction |

---

## Core Sentence

~~~text
A model is not wrong because it closes locally.
A model becomes structurally wrong when it is used beyond the scope where its closure remains valid.
~~~
