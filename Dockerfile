FROM python:3.7.3-slim-stretch as base

# install system dependencies
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      build-essential \
      libsqlite3-dev \
      make \
      python3-dev \
      && apt-get clean && rm -rf /var/lib/apt/lists/*

# upgrade pip, and install poetry
RUN pip install --upgrade pip
RUN pip install poetry==0.12.17

# Set up and become kip user
RUN useradd -u 1000 -m kip
USER kip

# create and switch to src work directory
RUN mkdir /home/kip/src
WORKDIR /home/kip/src

# copy server setup files
COPY --chown=kip:kip pyproject.toml .
COPY --chown=kip:kip poetry.lock .

# install python packages using poetry
RUN poetry install

# copy remaining files
COPY --chown=kip:kip Makefile .
COPY --chown=kip:kip server server

# copy all required files for testing
COPY --chown=kip:kip MANIFEST.in .
COPY --chown=kip:kip mypy.ini .
COPY --chown=kip:kip pytest.ini .
COPY --chown=kip:kip tox.ini .

# expose endpoint
EXPOSE 5000

########

# pick up from base
FROM base as flask-dev

# run make flask to start the server
ENTRYPOINT make flask

########

FROM node:latest as react-dev

# switch to node user given we're using the node base image
USER node

# create and switch to src directory
RUN mkdir /home/node/src
WORKDIR /home/node/src

# expose endpoint
EXPOSE 3000

# copy client setup files
COPY --chown=node:node Makefile .
COPY --chown=node:node client client

# install node packages using npm
RUN npm install

# run make react to start the client
ENTRYPOINT make react

########

FROM base as test

# run tox to go through pylint, mypy, and pytest
ENTRYPOINT tox
