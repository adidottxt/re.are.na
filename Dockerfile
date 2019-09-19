FROM python:3.7.3-slim-stretch as base

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      build-essential \
      libsqlite3-dev \
      make \
      python3-dev \
      && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN useradd -u 1000 -m kip
USER kip

RUN mkdir /home/kip/src
WORKDIR /home/kip/src

COPY --chown=kip:kip requirements.txt .
COPY --chown=kip:kip README.md .
COPY --chown=kip:kip Makefile .

COPY --chown=kip:kip server server

EXPOSE 5000

RUN pip install --user -r requirements.txt

########

FROM base as flask

ENTRYPOINT make flask

########

FROM node:latest as node

RUN useradd -u 1001 -m kip2
USER kip2

RUN mkdir /home/kip2/src
WORKDIR /home/kip2/src

COPY --chown=kip2:kip2 Makefile .
COPY --chown=kip2:kip2 client client

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
