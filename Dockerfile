FROM python:3.13.0-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.4

ENV PATH="/root/.local/bin:$PATH"

LABEL authors="danielvink"
RUN useradd -m daniel
WORKDIR /home/daniel

RUN pip install --upgrade pip
RUN pip install poetry

COPY src /home/daniel/src
COPY poetry.lock /home/daniel/poetry.lock
COPY pyproject.toml /home/daniel/pyproject.toml
RUN poetry install --no-root --without dev

USER daniel
CMD ["poetry", "run", "fastapi", "run", "src/sequences/main.py"]