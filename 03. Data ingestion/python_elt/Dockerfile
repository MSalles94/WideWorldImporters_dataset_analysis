FROM python:3.12.1-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .
 