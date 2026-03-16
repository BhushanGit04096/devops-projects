FROM python:3.9-slim

USER root

RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    mkdir -p /.local && \
    mkdir -p /.cache/pip && \
    chmod -R 777 /.local && \
    chmod -R 777 /.cache/pip

WORKDIR /workspace
