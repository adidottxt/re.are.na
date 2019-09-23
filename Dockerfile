FROM python:3.7.3-slim-stretch as base

RUN apt-get update -y && apt-get install -yq \
      build-essential \
      libsqlite3-dev \
      make \
      python3-dev \
      && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
# RUN pip install poetry==0.12.17

RUN useradd -u 1000 -m kip
USER kip

RUN mkdir /home/kip/src
WORKDIR /home/kip/src

COPY --chown=kip:kip requirements.txt .
COPY --chown=kip:kip README.md .
COPY --chown=kip:kip Makefile .
# COPY --chown=kip:kip pyproject.toml .
# COPY --chown=kip:kip poetry.lock .

COPY --chown=kip:kip server server

EXPOSE 5000

RUN pip install --user -r requirements.txt
# RUN poetry config settings.virtualenvs.create false
# RUN poetry install

########

FROM base as flask

ENTRYPOINT make flask

########

FROM node:latest as node

USER node

RUN mkdir /home/node/src
WORKDIR /home/node/src

COPY --chown=node:node Makefile .
COPY --chown=node:node client client

EXPOSE 3000

########

FROM node as react

RUN npm install

ENTRYPOINT make react

########

FROM base as test

COPY --chown=kip:kip MANIFEST.in .
COPY --chown=kip:kip mypy.ini .
COPY --chown=kip:kip pytest.ini .
COPY --chown=kip:kip tox.ini .

ENTRYPOINT tox
