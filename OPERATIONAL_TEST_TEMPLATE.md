# Operational Test Template

Use this template to test the law on a real case.

## 1. Object / Manifestation

~~~text
x =
~~~

What is being treated?

## 2. Framework

~~~text
F =
~~~

What model, theory, discipline, algorithm, answer, diagnosis, or decision is being used?

## 3. Use

~~~text
U =
~~~

How is F actually being used?

## 4. Local Closure

~~~text
LocalClosureF(x) =
~~~

What does F treat as settled, complete, classified, calculated, or decided?

## 5. Valid Scope

~~~text
ValidScope(F,x) =
~~~

Where is F valid?

## 6. Actual Use

~~~text
ActualUseU(F,x) =
~~~

Does actual use exceed valid scope?

## 7. Determinability Conditions

~~~text
Candidate DetCondΩ(d,x) =
~~~

What conditions make x determinable as x?

## 8. Critical Conditions for Use

~~~text
CriticalDepΩ(d,x,U) =
~~~

Which conditions are necessary for this use?

## 9. Excluded Conditions

~~~text
ExcludedF(d) =
~~~

Which critical conditions are excluded by F?

## 10. Structural Error Test

~~~text
ErrΩ(x,F,U) =
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

Result:

~~~text
YES / NO / UNDETERMINED
~~~

## 11. Correction

~~~text
CORR =
~~~

Possible corrections:

~~~text
declare scope
restrict use
add missing condition
change model
change data
change decision
open field
~~~
