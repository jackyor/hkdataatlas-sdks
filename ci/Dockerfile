FROM oven/bun:1.4.3@sha256:ec06c3b6cea04192ae6770c434f668ca41d343ad19fa6472216c7b48be39c598 AS bun
FROM ghcr.io/astral-sh/uv:0.13.5@sha256:32a7bb39b496babbd997b0a39a4d66c126bdaf5661b302bf6f06abda8deca6ff AS uv
FROM node:24.22.1-bookworm-slim@sha256:be8204d4bd327363357f532187b752ff62759c31bedf98e9e18fc08c9cbd605c
COPY --from=bun /usr/local/bin/bun /usr/local/bin/bun
COPY --from=uv /uv /uvx /usr/local/bin/
ENV UV_PYTHON=3.14.9 UV_PYTHON_PREFERENCE=only-managed UV_PYTHON_DOWNLOADS=automatic
WORKDIR /work
# Dependency layers depend only on pinned manifests, not specifications or SDK output.
COPY package.json bun.lock pyproject.toml uv.lock .python-version ./
RUN bun install --ignore-scripts --frozen-lockfile
RUN uv sync --frozen
COPY . .
