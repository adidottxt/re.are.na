# 🥴 Three (are.na) Blocks A Day
a web app that serves up three random blocks from your are.na profile.<br>
a readwise for are.na blocks, if you will.<br>
(three blocks a day keeps the doctor away...?)

### 🛠 things to do
- <b>BACKEND</b>
  * Database work
    + set up mutations to allow database to be written to with graphql
    + use GraphQL functions within `blocks.py` functions
      - when given a new ID, check for both channel + block ID within db
      - store 3 ids in a database such that you do not see the same block twice
  * To send to front end:
    + get data of all three blocks
    + get class of all three blocks, present them accordingly
- <b>FRONTEND</b>
  * refresh should give you three new blocks
  * depending on block class, create type-specific components
- <b>SOME DAY...</b>
  * convert this to have the three blocks be emailed on a daily basis to myself
