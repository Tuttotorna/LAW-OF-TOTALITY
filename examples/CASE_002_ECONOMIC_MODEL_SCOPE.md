# CASE 002 — Economic Model Scope

## Object

~~~text
x = economic forecast or optimization model
~~~

## Framework

~~~text
F = simplified economic model
~~~

## Use

~~~text
U = policy, investment, or institutional decision based on the model
~~~

## Local Closure

~~~text
LocalClosureF(x) = the model produces a clean output under its assumptions
~~~

This can be valid inside the model.

## Valid Scope

~~~text
ValidScope(F,x) = conditions where assumptions remain approximately stable
~~~

## Scope Violation

~~~text
ActualUseU(F,x) exceeds ValidScope(F,x)
~~~

The model is used as if its assumptions covered the real decision field.

## Critical Excluded Dependence

Examples:

~~~text
liquidity shock
political constraint
energy dependency
supply-chain fragility
time delay
nonlinear behavioral reaction
institutional trust
~~~

## Diagnosis

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

The forecast becomes structurally invalid when the decision requires dependencies excluded by the model.

## Correction

~~~text
Keep the model local.
State valid scope.
Map excluded critical dependencies.
Do not convert model output into total decision authority.
~~~
