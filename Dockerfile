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

RUN ls -la
RUN pip freeze
RUN echo 'Setup done!'

########

FROM base as flask

RUN echo 'Setting up back-end...'
ENTRYPOINT make flask
