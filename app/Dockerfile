FROM python:3.10

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install --no-root --only main

COPY ./devops /app/devops

CMD ["poetry", "run", "start-app"]
