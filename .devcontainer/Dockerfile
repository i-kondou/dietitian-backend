FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
   curl \
   gnupg2 \
   ca-certificates \
 && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
 && apt-get install -y --no-install-recommends nodejs \
 && rm -rf /var/lib/apt/lists/*

ENV UV_INSTALL_DIR=/usr/local/bin
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN npm install -g pyright

WORKDIR /workspace
