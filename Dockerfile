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

# Set up and become adi user
RUN useradd -u 1000 -m adi
USER adi

# create and switch to src work directory
RUN mkdir /home/adi/src
WORKDIR /home/adi/src

# copy server setup files
COPY --chown=adi:adi pyproject.toml .
COPY --chown=adi:adi poetry.lock .

# install python packages using poetry
RUN poetry install

# copy remaining files
COPY --chown=adi:adi Makefile .
COPY --chown=adi:adi server server

# copy all required files for testing
COPY --chown=adi:adi MANIFEST.in .
COPY --chown=adi:adi mypy.ini .
COPY --chown=adi:adi pytest.ini .
COPY --chown=adi:adi tox.ini .

# expose endpoint
EXPOSE 5000

########

# pick up from base
FROM base as server

# run make flask to start the server
ENTRYPOINT make server

########

FROM node:latest as client

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
ENTRYPOINT make client

########

FROM base as test

# run tox to go through pylint, mypy, and pytest
ENTRYPOINT tox
