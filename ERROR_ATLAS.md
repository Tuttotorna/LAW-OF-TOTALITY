# Error Atlas — v0.6.0

## Purpose

This file is the empirical case layer of the Law of Totality.

It does not claim that the repository has already proven a universal law.

It shows that the same structural error pattern can be mapped across many domains:

    local closure
    + use beyond valid scope
    + excluded critical dependency
    = structural error

The goal is to make the scope visible through cases rather than through proclamation.

## Core Formula

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

## Atlas Status

Total cases: 45
Positive structural-error cases: 40
Negative control cases: 5
Domains represented: 40

Domains:

- AI
- AI / Law
- Algorithmic Governance
- Anthropology
- Business
- Culture
- Data Science
- Decision Theory
- Economics
- Economics / Ideology
- Education
- Engineering
- Epistemology
- Forecasting
- History
- Institutions
- Justice / Social Control
- Language
- Law
- Mathematics / Representation
- Media
- Medicine
- Medicine / Systems
- Memory
- Military / Security
- Model Risk
- Navigation
- Negative Control
- Political Theory
- Politics
- Psychology
- Relationships
- Religion / Anthropology
- Science
- Social Identity
- Social Systems
- Software / Safety
- Statistics
- Systems
- Technology

## Reading Rule

A case is not included to prove that the Law of Totality explains the full content of the object.

A case is included to show that once an object is treated through a finite framework for a concrete use, the law can explain the validity or invalidity of that treatment.

In compact form:

    The law does not explain every thing as total content.
    It explains the structural validity of every finite treatment submitted to it.

## Cases

### 1. Generic AI legal answer used as binding legal action

Status: STRUCTURAL ERROR

Domain: AI / Law

Case ID: ai_generic_legal_answer_as_binding_action

Object x:

    legal situation

Framework F:

    generic LLM-generated legal explanation

Actual use U:

    file, sign, or act on a binding legal decision

Valid scope:

    general informational orientation only

Excluded critical dependencies:

- jurisdiction
- dates
- court rules
- full documents
- licensed legal review

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    reduce the answer to general information or add jurisdiction-specific professional review

Trajectory change:

    prevents a plausible answer from becoming an invalid legal action

### 2. Single medical test treated as total diagnosis

Status: STRUCTURAL ERROR

Domain: Medicine

Case ID: medical_single_test_as_total_diagnosis

Object x:

    patient condition

Framework F:

    one laboratory value or one imaging result

Actual use U:

    definitive diagnosis and treatment decision

Valid scope:

    partial indicator inside clinical evaluation

Excluded critical dependencies:

- symptoms
- history
- differential diagnosis
- comorbidities
- contraindications

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    restore full clinical context before treatment

Trajectory change:

    prevents partial evidence from becoming total medical certainty

### 3. Financial model used outside its validation distribution

Status: STRUCTURAL ERROR

Domain: Model Risk

Case ID: financial_model_outside_distribution

Object x:

    market or credit risk

Framework F:

    model validated on historical distribution

Actual use U:

    deployment during shifted market conditions

Valid scope:

    conditions similar to validation assumptions

Excluded critical dependencies:

- distribution shift
- liquidity regime
- new correlations
- feedback effects
- stress scenario

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    restrict use, revalidate, stress-test, and monitor drift

Trajectory change:

    prevents local statistical validity from becoming systemic financial exposure

### 4. Simplified engineering formula used outside assumptions

Status: STRUCTURAL ERROR

Domain: Engineering

Case ID: engineering_formula_outside_assumptions

Object x:

    physical structure

Framework F:

    idealized simplified calculation

Actual use U:

    real-world deployment under variable load

Valid scope:

    declared ideal or bounded operating assumptions

Excluded critical dependencies:

- fatigue
- temperature
- material defects
- dynamic loads
- tolerances

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    declare assumptions, test edge conditions, add safety factor

Trajectory change:

    prevents calculation correctness from becoming structural failure

### 5. School grade treated as total value of a student

Status: STRUCTURAL ERROR

Domain: Education

Case ID: school_grade_as_total_human_value

Object x:

    student

Framework F:

    grade or standardized score

Actual use U:

    judge intelligence, future worth, or human potential

Valid scope:

    limited measurement of performance under specific conditions

Excluded critical dependencies:

- context
- health
- motivation
- teaching quality
- creativity
- late development

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat the grade as one indicator, not identity

Trajectory change:

    prevents a metric from becoming a life-defining closure

### 6. Political ideology treated as total explanation

Status: STRUCTURAL ERROR

Domain: Politics

Case ID: political_ideology_as_total_explanation

Object x:

    society

Framework F:

    single ideological framework

Actual use U:

    explain and decide all social problems

Valid scope:

    partial interpretive and policy lens

Excluded critical dependencies:

- history
- economics
- culture
- incentives
- institutions
- human behavior

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    force multi-framework dependency audit before policy closure

Trajectory change:

    prevents ideological reduction from becoming governance error

### 7. Religious dogma treated as total cosmic explanation

Status: STRUCTURAL ERROR

Domain: Religion / Anthropology

Case ID: religious_dogma_as_total_cosmic_explanation

Object x:

    reality, suffering, origin, meaning

Framework F:

    closed dogmatic narrative

Actual use U:

    explain all existence and impose conduct

Valid scope:

    symbolic, communal, ritual, or existential interpretation

Excluded critical dependencies:

- empirical evidence
- plural interpretations
- historical formation
- psychology
- power structures

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    distinguish symbolic use from total explanatory authority

Trajectory change:

    prevents narrative closure from becoming absolute domination of meaning

### 8. Bureaucratic rule treated as justice

Status: STRUCTURAL ERROR

Domain: Institutions

Case ID: bureaucratic_rule_as_justice

Object x:

    human case

Framework F:

    administrative rule

Actual use U:

    produce just outcome

Valid scope:

    standardized procedural handling

Excluded critical dependencies:

- exception
- harm
- context
- proportionality
- human consequence

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    add exception review and consequence audit

Trajectory change:

    prevents procedural correctness from becoming structural injustice

### 9. Single KPI treated as company truth

Status: STRUCTURAL ERROR

Domain: Business

Case ID: kpi_as_company_truth

Object x:

    business system

Framework F:

    one metric such as revenue, growth, or engagement

Actual use U:

    strategic decision about company health

Valid scope:

    bounded measurement of one dimension

Excluded critical dependencies:

- customer trust
- burnout
- legal risk
- hidden costs
- long-term resilience

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    use KPI as local signal inside multi-dimensional audit

Trajectory change:

    prevents metric optimization from damaging the actual system

### 10. Single episode treated as total identity of a person

Status: STRUCTURAL ERROR

Domain: Relationships

Case ID: relationship_single_episode_as_identity

Object x:

    person

Framework F:

    one episode, sentence, mistake, or reaction

Actual use U:

    define the person's entire character

Valid scope:

    local evidence about one moment

Excluded critical dependencies:

- history
- stress
- pattern frequency
- intent
- change over time
- context

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate episode evidence from total identity judgment

Trajectory change:

    prevents human relation from collapsing into fragmentary judgment

### 11. Winner narrative treated as total history

Status: STRUCTURAL ERROR

Domain: History

Case ID: historical_winner_narrative_as_total_history

Object x:

    historical event

Framework F:

    dominant historical narrative

Actual use U:

    define collective memory and moral interpretation

Valid scope:

    one perspective or archive tradition

Excluded critical dependencies:

- loser records
- material causes
- minority accounts
- economic context
- propaganda

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    reconstruct multi-perspective dependency field

Trajectory change:

    prevents historical memory from becoming political closure

### 12. Map used outside its valid scale

Status: STRUCTURAL ERROR

Domain: Navigation

Case ID: map_used_outside_scale

Object x:

    territory

Framework F:

    tourist city map

Actual use U:

    mountain rescue navigation in winter

Valid scope:

    urban tourist navigation

Excluded critical dependencies:

- altitude
- snow
- terrain risk
- weather exposure
- route duration

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    use a terrain/weather/navigation framework fit for the actual route

Trajectory change:

    prevents map correctness from becoming route danger

### 13. Dataset treated as reality

Status: STRUCTURAL ERROR

Domain: Data Science

Case ID: dataset_as_reality

Object x:

    population or phenomenon

Framework F:

    available dataset

Actual use U:

    general claim about reality

Valid scope:

    inference over represented population under sampling assumptions

Excluded critical dependencies:

- sampling bias
- missing population
- measurement process
- time drift
- data collection incentives

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    declare dataset scope and missing population before generalization

Trajectory change:

    prevents data availability from masquerading as reality coverage

### 14. Average treated as individual truth

Status: STRUCTURAL ERROR

Domain: Statistics

Case ID: average_as_individual_truth

Object x:

    individual case

Framework F:

    population average

Actual use U:

    decide what is true for a specific individual

Valid scope:

    aggregate tendency

Excluded critical dependencies:

- variance
- distribution tails
- individual context
- subgroup membership
- causal mechanism

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    move from aggregate statistic to case-specific evaluation

Trajectory change:

    prevents population signal from erasing individual reality

### 15. Legal text treated as total justice

Status: STRUCTURAL ERROR

Domain: Law

Case ID: law_text_as_total_justice

Object x:

    legal-human conflict

Framework F:

    literal legal text

Actual use U:

    produce justice

Valid scope:

    rule application within legal interpretation

Excluded critical dependencies:

- purpose
- precedent
- equity
- specific facts
- human consequences

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate legality, interpretation, proportionality, and justice impact

Trajectory change:

    prevents formal legal closure from becoming unjust outcome

### 16. Intelligence fragment treated as strategy

Status: STRUCTURAL ERROR

Domain: Military / Security

Case ID: military_intelligence_fragment_as_strategy

Object x:

    conflict situation

Framework F:

    partial intelligence report

Actual use U:

    strategic action

Valid scope:

    one evidence stream under uncertainty

Excluded critical dependencies:

- enemy adaptation
- logistics
- civilian impact
- misinformation
- political consequence

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat intelligence as one input inside adversarial multi-factor analysis

Trajectory change:

    prevents partial intelligence from becoming strategic disaster

### 17. Economic growth treated as total social good

Status: STRUCTURAL ERROR

Domain: Economics

Case ID: economic_growth_as_social_good

Object x:

    society

Framework F:

    GDP or growth indicator

Actual use U:

    judge societal success

Valid scope:

    economic output measurement

Excluded critical dependencies:

- inequality
- health
- ecology
- distribution
- quality of life
- future debt

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    evaluate growth inside a wider dependency field

Trajectory change:

    prevents output expansion from being mistaken for human improvement

### 18. Algorithmic score treated as person

Status: STRUCTURAL ERROR

Domain: Algorithmic Governance

Case ID: algorithmic_score_as_person

Object x:

    human being

Framework F:

    risk score or ranking algorithm

Actual use U:

    access, punishment, employment, insurance, credit, or policing decision

Valid scope:

    bounded probabilistic indicator under model assumptions

Excluded critical dependencies:

- data provenance
- context
- bias
- appeal
- causal explanation
- changed circumstances

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    require explanation, contestability, human review, and scope limits

Trajectory change:

    prevents model output from replacing human reality

### 19. Scientific model treated as the object itself

Status: STRUCTURAL ERROR

Domain: Science

Case ID: scientific_model_as_the_object

Object x:

    natural phenomenon

Framework F:

    scientific model

Actual use U:

    claim total identity with reality

Valid scope:

    predictive or explanatory domain under assumptions

Excluded critical dependencies:

- boundary conditions
- unmodeled variables
- scale
- measurement limits
- alternative mechanisms

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat model as valid representation under scope, not the object itself

Trajectory change:

    prevents scientific success from hardening into false ontology

### 20. Reputation treated as truth

Status: STRUCTURAL ERROR

Domain: Social Systems

Case ID: social_reputation_as_truth

Object x:

    person or group

Framework F:

    social reputation

Actual use U:

    judge reality, guilt, competence, or worth

Valid scope:

    social signal of how others currently perceive x

Excluded critical dependencies:

- evidence
- incentives
- rumor dynamics
- power relations
- context
- time

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate reputation from evidence and direct verification

Trajectory change:

    prevents collective perception from becoming truth

### 21. News headline treated as complete event

Status: STRUCTURAL ERROR

Domain: Media

Case ID: news_headline_as_complete_event

Object x:

    public event

Framework F:

    headline or short news frame

Actual use U:

    form stable judgment

Valid scope:

    attention trigger and compressed summary

Excluded critical dependencies:

- full article
- source incentives
- timeline
- missing actors
- uncertainty
- context

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    delay judgment until context and dependencies are restored

Trajectory change:

    prevents compression from becoming public misconception

### 22. Emotion treated as total reality

Status: STRUCTURAL ERROR

Domain: Psychology

Case ID: emotion_as_total_reality

Object x:

    situation

Framework F:

    current emotional state

Actual use U:

    decide what is true or irreversible

Valid scope:

    signal of current internal state

Excluded critical dependencies:

- time
- evidence
- body state
- stressors
- alternative interpretations
- future change

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    use emotion as data, not as total verdict

Trajectory change:

    prevents temporary state from becoming permanent decision

### 23. Memory treated as recording

Status: STRUCTURAL ERROR

Domain: Memory

Case ID: memory_as_recording

Object x:

    past event

Framework F:

    personal memory

Actual use U:

    establish exact historical truth

Valid scope:

    subjective reconstruction and experiential evidence

Excluded critical dependencies:

- memory distortion
- other witnesses
- documents
- time
- emotional reconstruction

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat memory as evidence requiring corroboration

Trajectory change:

    prevents personal certainty from becoming false historical closure

### 24. Tradition treated as proof

Status: STRUCTURAL ERROR

Domain: Culture

Case ID: tradition_as_proof

Object x:

    practice or belief

Framework F:

    tradition

Actual use U:

    justify truth, morality, or permanence

Valid scope:

    evidence of historical continuity and cultural meaning

Excluded critical dependencies:

- origin
- harm
- changed conditions
- power structures
- alternative values

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate continuity from validity

Trajectory change:

    prevents inherited closure from blocking correction

### 25. Technology treated as progress

Status: STRUCTURAL ERROR

Domain: Technology

Case ID: technology_as_progress

Object x:

    new technical capability

Framework F:

    performance or novelty metric

Actual use U:

    declare social improvement

Valid scope:

    technical capability assessment

Excluded critical dependencies:

- misuse
- inequality
- side effects
- dependency
- governance
- human adaptation

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    evaluate deployment consequences, not only capability

Trajectory change:

    prevents capability increase from being mistaken for civilizational improvement

### 26. Market mechanism treated as total order

Status: STRUCTURAL ERROR

Domain: Economics / Ideology

Case ID: free_market_as_total_order

Object x:

    society and resource distribution

Framework F:

    market price mechanism

Actual use U:

    decide all social allocation problems

Valid scope:

    exchange coordination under assumptions

Excluded critical dependencies:

- externalities
- power asymmetry
- public goods
- information asymmetry
- basic rights

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat markets as one coordination framework inside institutional constraints

Trajectory change:

    prevents economic mechanism from becoming total social philosophy

### 27. Central plan treated as total order

Status: STRUCTURAL ERROR

Domain: Economics / Ideology

Case ID: central_plan_as_total_order

Object x:

    society and production

Framework F:

    central planning framework

Actual use U:

    decide all allocation, production, and social coordination

Valid scope:

    bounded coordination under available information and enforceable aims

Excluded critical dependencies:

- local knowledge
- incentives
- adaptation
- freedom
- feedback delays
- corruption

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    restore feedback, plural mechanisms, and limits of central visibility

Trajectory change:

    prevents planning abstraction from replacing living complexity

### 28. Expert authority treated as total truth

Status: STRUCTURAL ERROR

Domain: Epistemology

Case ID: expert_authority_as_total_truth

Object x:

    claim or decision

Framework F:

    expert authority

Actual use U:

    settle truth outside declared expertise or evidence

Valid scope:

    specialized judgment within domain and evidence

Excluded critical dependencies:

- field boundary
- uncertainty
- conflicts of interest
- data quality
- minority technical objections

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    use expertise as weighted input inside scope, not absolute closure

Trajectory change:

    prevents authority from replacing validity

### 29. Majority preference treated as truth or justice

Status: STRUCTURAL ERROR

Domain: Political Theory

Case ID: democratic_majority_as_truth

Object x:

    collective decision

Framework F:

    majority vote

Actual use U:

    define truth, justice, or rights

Valid scope:

    legitimate collective decision procedure under constitutional limits

Excluded critical dependencies:

- minority rights
- truth conditions
- long-term harm
- manipulation
- information quality

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate procedural legitimacy from truth and justice validity

Trajectory change:

    prevents procedure from becoming moral absolution

### 30. External success treated as human value

Status: STRUCTURAL ERROR

Domain: Anthropology

Case ID: personal_success_as_human_value

Object x:

    person

Framework F:

    wealth, status, title, productivity, recognition

Actual use U:

    define human worth

Valid scope:

    limited social or economic signal

Excluded critical dependencies:

- character
- suffering
- care
- integrity
- context
- unrecognized contribution

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate measurable social outcome from human value

Trajectory change:

    prevents civilization from confusing visibility with worth

### 31. Punishment treated as solution

Status: STRUCTURAL ERROR

Domain: Justice / Social Control

Case ID: punishment_as_solution

Object x:

    harmful behavior

Framework F:

    punitive response

Actual use U:

    solve the cause of harm

Valid scope:

    deterrence, containment, accountability in bounded conditions

Excluded critical dependencies:

- root causes
- rehabilitation
- social context
- recidivism
- victim restoration

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    distinguish containment, accountability, prevention, and repair

Trajectory change:

    prevents punitive closure from replacing structural prevention

### 32. Symptom suppression treated as cure

Status: STRUCTURAL ERROR

Domain: Medicine / Systems

Case ID: symptom_suppression_as_cure

Object x:

    illness or system dysfunction

Framework F:

    symptom-reducing intervention

Actual use U:

    declare underlying problem solved

Valid scope:

    local relief or stabilization

Excluded critical dependencies:

- root cause
- recurrence
- systemic drivers
- side effects
- long-term trajectory

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate relief from cure and track underlying dependencies

Trajectory change:

    prevents temporary stabilization from being mistaken for resolution

### 33. Formal correctness treated as system safety

Status: STRUCTURAL ERROR

Domain: Software / Safety

Case ID: formal_correctness_as_system_safety

Object x:

    software-controlled system

Framework F:

    formal software verification

Actual use U:

    declare complete operational safety

Valid scope:

    properties proven inside specified formal model

Excluded critical dependencies:

- requirements correctness
- human interaction
- hardware faults
- environment
- unexpected use

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    connect formal proof to system-level hazard analysis

Trajectory change:

    prevents proof inside model from becoming false safety of the whole

### 34. Label treated as essence

Status: STRUCTURAL ERROR

Domain: Language

Case ID: language_label_as_essence

Object x:

    person, group, object, or phenomenon

Framework F:

    linguistic label

Actual use U:

    define essence or total meaning

Valid scope:

    communication shorthand

Excluded critical dependencies:

- variation
- history
- context
- individual reality
- semantic ambiguity

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    treat label as pointer, not essence

Trajectory change:

    prevents naming from becoming ontological imprisonment

### 35. Prediction treated as future

Status: STRUCTURAL ERROR

Domain: Forecasting

Case ID: prediction_as_future

Object x:

    future event

Framework F:

    forecast model

Actual use U:

    act as if forecast is certain

Valid scope:

    probabilistic scenario under assumptions

Excluded critical dependencies:

- uncertainty
- feedback effects
- model error
- unknown unknowns
- intervention changes

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    convert prediction into scenario planning with confidence and contingencies

Trajectory change:

    prevents probability from becoming fatalism

### 36. Identity category treated as person

Status: STRUCTURAL ERROR

Domain: Social Identity

Case ID: identity_category_as_person

Object x:

    individual

Framework F:

    group category

Actual use U:

    judge the individual

Valid scope:

    broad sociological or demographic descriptor

Excluded critical dependencies:

- individual variation
- life history
- agency
- context
- personal evidence

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    restore individual field beyond category membership

Trajectory change:

    prevents category cognition from becoming prejudice

### 37. Short-term optimization treated as long-term good

Status: STRUCTURAL ERROR

Domain: Decision Theory

Case ID: short_term_optimization_as_long_term_good

Object x:

    decision trajectory

Framework F:

    short-term objective function

Actual use U:

    maximize long-term system outcome

Valid scope:

    local immediate objective

Excluded critical dependencies:

- future fragility
- maintenance
- adaptation
- externalities
- second-order effects

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    add temporal dependency and long-term stability audit

Trajectory change:

    prevents local gain from producing global deterioration

### 38. Representation in one base treated as the number itself

Status: STRUCTURAL ERROR

Domain: Mathematics / Representation

Case ID: object_seen_from_one_base_as_object_itself

Object x:

    mathematical object

Framework F:

    one representation, base, notation, or projection

Actual use U:

    claim total property of the object

Valid scope:

    representation-specific observation

Excluded critical dependencies:

- invariance
- other representations
- base-dependence
- transformation behavior

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    compare across representations before claiming object-level property

Trajectory change:

    prevents representational artifact from becoming false ontology

### 39. LLM confident tone treated as truth

Status: STRUCTURAL ERROR

Domain: AI

Case ID: llm_confidence_tone_as_truth

Object x:

    answer

Framework F:

    linguistically fluent model output

Actual use U:

    accept as verified fact

Valid scope:

    generated answer under model/source constraints

Excluded critical dependencies:

- source verification
- recency
- domain accuracy
- ambiguity
- high-stakes use

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    separate fluency from verification and scope

Trajectory change:

    prevents plausible language from becoming false knowledge

### 40. Local correctness treated as global stability

Status: STRUCTURAL ERROR

Domain: Systems

Case ID: local_correctness_as_global_stability

Object x:

    system

Framework F:

    component-level correctness

Actual use U:

    declare whole-system stability

Valid scope:

    behavior of component inside tested conditions

Excluded critical dependencies:

- interactions
- feedback
- load
- environment
- failure propagation

Structural reading:

    The framework may be locally useful or correct, but it becomes structurally invalid when used for this actual use while excluding the listed critical dependencies.

Correction:

    perform system-level interaction and stability audit

Trajectory change:

    prevents correct parts from hiding fragile wholes

### 41. City map used for city walk

Status: NO STRUCTURAL ERROR

Domain: Negative Control

Case ID: negative_control_city_map_for_city_walk

Object x:

    city center

Framework F:

    city tourist map

Actual use U:

    find a museum inside the mapped area

Valid scope:

    urban tourist navigation

Excluded critical dependencies:

- none identified for this use

Structural reading:

    No structural error is present because the actual use remains inside the valid scope, or the excluded dependencies are not critical for this use.

Correction:

    no correction needed beyond normal map-reading limits

Trajectory change:

    shows that local closure is valid when use stays inside scope

### 42. Rough estimate used only for brainstorming

Status: NO STRUCTURAL ERROR

Domain: Negative Control

Case ID: negative_control_rough_estimate_for_brainstorming

Object x:

    early project cost

Framework F:

    rough estimate

Actual use U:

    informal preliminary discussion

Valid scope:

    non-binding approximate orientation

Excluded critical dependencies:

- precise supplier quotes
- legal commitments
- cash-flow timing

Structural reading:

    No structural error is present because the actual use remains inside the valid scope, or the excluded dependencies are not critical for this use.

Correction:

    no structural error if not used for commitment

Trajectory change:

    shows that excluded dependencies are not errors unless critical for the actual use

### 43. Formula used inside its assumptions

Status: NO STRUCTURAL ERROR

Domain: Negative Control

Case ID: negative_control_formula_inside_assumptions

Object x:

    idealized physics problem

Framework F:

    declared ideal formula

Actual use U:

    solve classroom ideal case

Valid scope:

    ideal conditions explicitly stated

Excluded critical dependencies:

- real friction
- material defects
- measurement noise

Structural reading:

    No structural error is present because the actual use remains inside the valid scope, or the excluded dependencies are not critical for this use.

Correction:

    no correction needed while the use remains ideal and declared

Trajectory change:

    shows that abstraction is legitimate inside declared scope

### 44. Medical test used as partial indicator

Status: NO STRUCTURAL ERROR

Domain: Negative Control

Case ID: negative_control_medical_test_as_partial_indicator

Object x:

    patient condition

Framework F:

    single test result

Actual use U:

    decide what further tests or questions are needed

Valid scope:

    partial clinical indicator

Excluded critical dependencies:

- full history
- differential diagnosis
- contraindications

Structural reading:

    No structural error is present because the actual use remains inside the valid scope, or the excluded dependencies are not critical for this use.

Correction:

    no structural error if explicitly used only to guide further inquiry

Trajectory change:

    shows that partial evidence is safe when kept partial

### 45. LLM answer used as draft only

Status: NO STRUCTURAL ERROR

Domain: Negative Control

Case ID: negative_control_llm_answer_as_draft

Object x:

    draft explanation

Framework F:

    LLM-generated text

Actual use U:

    generate a first draft for later verification

Valid scope:

    drafting, brainstorming, provisional formulation

Excluded critical dependencies:

- source verification
- domain expert review
- recency check

Structural reading:

    No structural error is present because the actual use remains inside the valid scope, or the excluded dependencies are not critical for this use.

Correction:

    no structural error if not treated as verified output

Trajectory change:

    shows that AI output is not invalid by nature; misuse creates the error

## Conclusion

The atlas does not prove universality by assertion.

It demonstrates a repeated structure across domains:

    a thing is treated through a finite framework;
    the framework is used for a concrete purpose;
    the use requires dependencies the framework excludes;
    the result becomes structurally invalid.

This is the operational bridge from the formal law to real-world visibility.
