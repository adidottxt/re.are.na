# 🔁 re.are.na
A web app that serves up three blocks picked at random from your are.na
profile, in an attempt to enable spaced repetition for are.na blocks.

### Background
A [readwise](https://readwise.io/) for your are.na blocks, basically.<br>

### How to install
1. Clone this repository.
2. Create an application on are.na's [developer page](https://dev.are.na/oauth/applications), filling out the required
  information. When you're done, you should have a personal access token on
  the application's page (the link to which should look like
  this: `dev.are.na/oauth/applications/{APPLICATION NUMBER}`).
3. Create the file `re.are.na/flask-backend/pkg/config.py`, as below:
  ```
  ACCESS_TOKEN = 'your are.na personal access token here'
  ```
4. Run `./install.sh` to set up the application.

### How to run
- Assuming you've installed the application correctly, `./run.sh`. That's it.

### 🛠 Things to do
- REFACTOR:
  * update README.md with background
  * unit tests
  * tox
  * make the front end responsive
  * set up on docker?
  * longer term...
    + convert this to have this be a daily email as opposed to a web app
