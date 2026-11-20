# Phase 0 lesson 7, Mac-sized version of code/Dockerfile.
# The lesson's image uses nvidia/cuda (x86 only for the cu124 wheels, ~15-20 GB).
# A Mac has no CUDA, so this uses a small Linux image and the CPU build of
# the same PyTorch version. BASE lets exercise 4 compare two base images.
ARG BASE=python:3.12-slim
FROM ${BASE}

ENV PYTHONUNBUFFERED=1

# curl is for exercise 2 (calling Qdrant from inside the container)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir \
    torch==2.6.0 \
    --index-url https://download.pytorch.org/whl/cpu

RUN python -m pip install --no-cache-dir numpy

# Exercise 3: flask, added after the first build
RUN python -m pip install --no-cache-dir flask

WORKDIR /workspace
COPY app.py /workspace/app.py

EXPOSE 5000

CMD ["python"]
