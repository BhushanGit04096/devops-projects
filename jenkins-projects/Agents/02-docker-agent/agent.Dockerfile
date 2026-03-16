FROM python:3.9-slim

USER root

RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /workspace
