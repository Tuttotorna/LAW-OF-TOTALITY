# CASE 003 — Project Safety

## Object

~~~text
x = operational project plan
~~~

## Framework

~~~text
F = schedule / role / logistics plan
~~~

## Use

~~~text
U = real-world execution with people, risk, time, safety, equipment, authority, weather, and failure modes
~~~

## Local Closure

~~~text
LocalClosureF(x) = the plan appears complete on paper
~~~

This can be locally valid as a planning document.

## Valid Scope

~~~text
ValidScope(F,x) = coordination under expected conditions
~~~

## Scope Violation

~~~text
ActualUseU(F,x) exceeds ValidScope(F,x)
~~~

The plan is treated as execution-ready while critical dependencies remain unconfirmed.

## Critical Excluded Dependence

Examples:

~~~text
medical authority
rescue chain
weather window
navigation responsibility
equipment redundancy
role confirmation
communication protocol
fatigue management
contingency decision rights
~~~

## Diagnosis

~~~text
ErrΩ(x,F,U) = yes
~~~

if the project proceeds as if the local plan were complete while excluding a critical condition required for safe execution.

## Correction

~~~text
Separate idea from project.
Separate contact from confirmation.
Separate role name from operational responsibility.
Separate enthusiasm from structural readiness.
~~~

## Core Reading

~~~text
Correct on paper ≠ stable in execution.
~~~
