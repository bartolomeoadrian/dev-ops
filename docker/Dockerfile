# Etapa 1: Construcción (Build)
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Etapa 2: Pruebas
FROM builder AS tester

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

RUN . /opt/venv/bin/activate && \
    python -m unittest discover -s tests

# Etapa 3: Imagen final mínima
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

COPY . .

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]