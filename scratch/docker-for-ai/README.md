# Phase 0, lesson 7: Docker for AI (Mac version)

The lesson's `code/Dockerfile` starts from `nvidia/cuda:12.4.1-devel` and installs the CUDA build of PyTorch. That image is x86 only, about 15-20 GB, takes 30-60 minutes to build under emulation on Apple Silicon, and still has no GPU on a Mac. This folder does the same four exercises on a small Linux image with the CPU build of the same PyTorch version (2.6.0).

Run the commands from this folder: `cd scratch/docker-for-ai`

| File | What it is |
|---|---|
| `Dockerfile` | `python:3.12-slim` + PyTorch 2.6.0 (CPU) + NumPy + Flask + curl |
| `app.py` | A tiny Flask server for exercise 3 |
| `docker-compose.yml` | The lesson's stack (AI container + Qdrant) without the NVIDIA GPU reservation |

## Exercise 1: build and import PyTorch

```bash
docker build -t ai-dev-mac .
docker run --rm ai-dev-mac python -c "import torch; print(torch.__version__)"
```

Printed `2.6.0+cpu`. The lesson's check is a version starting with 2.6.0.

## Exercise 2: compose stack, Qdrant from the AI container

```bash
docker compose -p aiefs-lesson7 up -d
docker compose -p aiefs-lesson7 exec ai-dev curl http://qdrant:6333/collections
docker compose -p aiefs-lesson7 down
```

Reply: `{"result":{"collections":[]},"status":"ok",...}`. Inside the compose network the AI container finds the database by its service name, `qdrant`. Qdrant is empty, so the collection list is empty.

## Exercise 3: Flask server with a port mapping

```bash
docker run --rm -p 5001:5000 ai-dev-mac python app.py
```

Then open http://localhost:5001. Reply: `{"message":"Hello from inside the container","torch":"2.6.0+cpu"}`.

The lesson says `-p 5000:5000`, but port 5000 on a Mac belongs to macOS (AirPlay Receiver), so the Mac side is 5001. `-p 5001:5000` means "Mac port 5001 goes to container port 5000". The server listens on `0.0.0.0`: a server on `localhost` inside the container can't be reached from outside it.

## Exercise 4: image size by base image

```bash
docker build --build-arg BASE=python:3.12 -t ai-dev-mac:full .
docker images ai-dev-mac
```

| Image | Base | Size |
|---|---|---|
| `ai-dev-mac:latest` | `python:3.12-slim` | 1.05 GB |
| `ai-dev-mac:full` | `python:3.12` | 2.43 GB |

Same packages, 1.38 GB apart. The full base carries compilers, headers and extra system tools, the same thing the lesson's `devel` image carries over `runtime`. PyTorch is the biggest layer either way (591 MB, see `docker history ai-dev-mac`).

## Clean up

```bash
docker rmi ai-dev-mac:full ai-dev-mac
docker volume rm aiefs-lesson7_qdrant_data
```
