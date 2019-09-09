# 🔁 re.are.na
A web app that enables spaced repetition for Are.na blocks -- serving up three
random blocks from your profile.


### How to install
1. Clone this repository.
2. Create an application on [Are.na's developer page](https://dev.are.na/oauth/applications), filling out the required
  information. When you're done, you should have a personal access token on
  the application's page, and the link to said page should look like
  something like this: `dev.are.na/oauth/applications/{APPLICATION NUMBER}`.
3. Create the file `re.are.na/flask-backend/pkg/config.py`, as below:
  ```python
  ACCESS_TOKEN = 'your are.na personal access token here'
  ```
4. Run `./install.sh` to set up the application.


### How to run
- Run `./run.sh`.


### Background
[I've used Are.na](http://are.na/adi) for close to two years now. I've roughly created 100
channels and saved over 6000 blocks, and use it to organize all sorts
of content and resources.

Over that time, my use case for coming back to blocks I've already
saved has usually where I realize I've saved a resource that I need, or if
I'm looking for something in-depth to read or peruse.

As with most forms of research or reading, I've noticed that the most
interesting connections, learnings, and thoughts arise from coming back to a
block <i>well after</i> first adding the block to a channel. This, however,
would only really occur if I randomly stumbled into a block I added a few
weeks, months, or years ago.

The idea for this application came about when using [Readwise](https://readwise.io) -- a
product/service that essentially uses the technique of [Spaced Repetition](https://en.wikipedia.org/wiki/Spaced_repetition) to
make it easy to revisit Kindle highlights, resurfacing a few highlights back
to you via an email. I figured I could use a Readwise for are.na blocks,
which led me to this. Given the personal nature of this project, my initial
goal is to create a web app, and perhaps eventually create an email-based
service as well.
