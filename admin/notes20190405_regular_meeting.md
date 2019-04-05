# Respo 2019/04/05

## Front end

- This turned into a bit of brainstorming, and therefore these notes are quite chaotic. I apologize.

- A mockup exists

  - login

  - admin page: 

    - excel upload 3 files $\to$ database populated

    - adding competences $\to$ problematic

      generally, will not done be this way, only at first etc

    - we'll get rid of excels

  - user roles: 

    - admin (allowed to do batch stuff etc), 
    - HR (uses webapp), 
    - employees

  - a new employee: evaluated trough analytics?

    - workplace, employee: should be possible to query "which workplace is emp X best suited for?" to move employees around 
    - HR does the evaluation and enters it into the system
    - history: a line of events, click on it to see what it was - training X, some info about it
    - changes to data (new competence or something) need to be verified: by admin, perhaps some automation
    - ideally we'd have a fixed model of competences - but not now, we'll allow adding and removing competences

  - competences are periodic tables, adding new elements every now and then - grouped by alkaloid, metals, radioactive etc :smile:

  - current compromise: only the most power users are allowed to add competences - by including "competence requests" other users can ask admin to add stuff (might need a sup^sup^user role as well)

  - AI ideas to 'group competences' etc, ... :fire:

- we have top trainings, we have top competences

- employee can request any trainings, can accept/decline suggested trainings

- sorting users by lacking competences, see list of lacking 

- exchange of information regarding semars

  - sell to FIFA $$$

  ## Analytics:

  - some python is done
  - docs comming soon
  - ready to move on

  ## Data:

  - nothing new
  - training improves multiple competences - add to datamodel

  ## Dictionary (because we use many terms interchangingly and are often confused):

  - training (not seminar, education, etc)
  - 

