# Respo 2019/03/25

## Analytics - models

- optimistic vs pessimistic: if NaN or illegal, optimistic: it's fine, pessimistic: it's terrible

- $$Min(b_i/q_i) = relative\_lack$$,

  $$b_i$$ - mark, $$q_i$$ - req

  max is 1

- $$b_i-q_i = absolute\_lack$$

- basically, we have a working prototype of the algorithm

- currently we're testing using random fake data

- currently, output is 1 competence unless multiple have the same metric, return all highest

- currently, we're only using `min_req` and `current_mark`, not `importances`

## Analytics - Test data

- random data, diff distributions
- missing data
- very random data
- some real data
- math team: generate data, export csv
- backend team:  csv -> insert script sql

## Backend - Data

- Workplace - employee connection

## Arch

- arch: BD -> backend -> mid (analytics)-> frontend
- or:  BD -> backend + analytics -> frontend
- or:  BD -> backend -> frontend + analytics 
- Django: backend?? 
- Docker for deployment - is good, use
- Frontent: some JS ??

## Frontend

- mockups are coming
- colors and style are coming with mockups
- tech

## General:

- make folders for teams
- push stuff
- thx