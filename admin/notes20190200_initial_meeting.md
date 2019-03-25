# PKP sestanek 1

200h/5months. Each month at least 1h, otherwise is as it goes.

## Model kompetenc in sistem za podporo odločanja pri izboru izobraževanj

dr. Aleksander Zidanšek (MPŠ), dr. Bojan Cestnik (TEMIDA)

### Namen

Kompetence za delo so. 

Organzing competences:

- basic/generic
- specific
  - social, values, personal, strokovne kompetence

We want to measure kompetences and figure out which further education to recommend. (Optimization problem in a way) 

Vsak partner ima nabor kompetenc. Cilj je poenotiti abore kompetenc in sistem ocenjevanja kompetentnosti.

We got an Entity-Relanshionship diagram of competency. Basic: workplace, employee, competence, education. 

How to chose which seminars/education to select.

Measurements:

- importance of competence for a certain workplace: [1-10]
- level of competence for a cpecific competenc: [0-100]

Basically, a model is implemented in excell and we need it to be a (web)app

Finally, we want to plan employee's further education, including costs, and track results.

25.2. do 25.7. 

Tech:

- html, css, js, php, mysql (foss) (proposed)
- github

Plan:

- open issues:
  - nabor kompetenc - extendable?
- analiza, načrt: process model, data model, UI model
- second phase: implementation

## Methods

Agile RUP - Kroll & Kruchten: The rational unified process made easy

Less docs, ceremony, tho try to follow the philosphy:

- major risks early
- value for customer
- executable software
- ...

## Tasks:

1. Process model (UML, scenarios, use cases)
2. ERD logični mode podatkovni
3. UI: dashboard style
4. some smarter model on competences etc (bayes analisys, neural net???)
5. nabor komptetenc
6. impl podatkovnega modela
7. impl komponent
8. impl helper funkcij
9. integracija po proesnem modelu
10. testiranje
11. release???

Timeseries: we want to see history of competences per worker etc. Think input, storage, user friendlyness. Database per user - user is company - but we need to do for one company. 

Scenario:

- HR needs a list of seminars, competences, employees, wants to match them up.
- First approx is data from the past project

---

==1h is this meeting==

