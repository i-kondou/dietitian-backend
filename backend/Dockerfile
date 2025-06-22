FROM python:3.12-bullseye

WORKDIR /workspace/
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

ENV UV_INSTALL_DIR=/usr/local/bin
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY pyproject.toml uv.lock README.md /workspace/
COPY secrets/ /secrets/
RUN uv sync --frozen --python-preference=system

COPY src/ /workspace/src/
RUN uv pip install --system -e . \
&& uv pip install -qU langchain-google-genai \
&& uv pip install -qU pillow \
&& uv pip install -qU firebase-admin

EXPOSE 8080

ENTRYPOINT ["python", "-m", "uvicorn"]
CMD ["src.api:app", "--host", "0.0.0.0", "--port", "8080"]
