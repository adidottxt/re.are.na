FROM python:3.7.3-slim-stretch

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      build-essential \
      git \
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

# COPY --chown=kip:kip pyproject.toml .
# COPY --chown=kip:kip poetry.lock .
COPY --chown=kip:kip requirements.txt .
COPY --chown=kip:kip README.md .
COPY --chown=kip:kip Makefile .
COPY --chown=kip:kip tox.ini .
COPY --chown=kip:kip pytest.ini .
COPY --chown=kip:kip mypy.ini .
COPY --chown=kip:kip setup.py .
COPY --chown=kip:kip MANIFEST.in .

COPY --chown=kip:kip server server
COPY --chown=kip:kip client client

EXPOSE 5000

RUN pip install --user -r requirements.txt

RUN ls -la
RUN pip freeze

ENTRYPOINT make flask
