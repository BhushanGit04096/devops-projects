# Jenkins CI/CD Pipeline for a Dockerized Python Application

This project demonstrates a **complete CI/CD pipeline using Jenkins, Docker, and Docker Compose** for a simple Python application. It shows how source code can be automatically built, tested, containerized, and deployed using Jenkins.

---

## Overview

The goal of this project is to demonstrate a basic **CI/CD workflow** with the following steps:

- Build and test a Python application
- Containerize the application using Docker
- Run the container using Docker Compose
- Automate the pipeline using Jenkins
- Push the Docker image to Docker Hub

The application itself is a simple **Hello World Python program** with a unit test written using Python's `unittest` framework.

---

## Project Structure

```
python-jenkins-docker/
│
├── app.py
├── tests/
│   └── test_app.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

### Files Description

| File | Purpose |
|-----|--------|
| `app.py` | Main Python application |
| `tests/test_app.py` | Unit tests for the application |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Defines the Docker image |
| `docker-compose.yml` | Runs the containerized application |
| `Jenkinsfile` | Jenkins CI/CD pipeline configuration |

---

## Running the Application Locally

Run the application directly:

```bash
python app.py
```

Expected output:

```
Hello from Python Application for Jenkins CI/CD!
```

---

## Running Tests

Run unit tests using:

```bash
python -m unittest discover tests
```

---

## Running with Docker

Build Docker image:

```bash
docker build -t python-jenkins-docker .
```

Run container:

```bash
docker run python-jenkins-docker
```

---

## Running with Docker Compose

Start the service:

```bash
docker-compose up --build
```

Stop the service:

```bash
docker-compose down
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Build** – Validate Python code
2. **Test** – Run unit tests
3. **Docker Build** – Build Docker image
4. **Docker Push** – Push image to Docker Hub
5. **Run Container** – Execute the containerized application

Pipeline defined in `Jenkinsfile`.

---

## Prerequisites

Before running this project, install:

- Python 3.x
- Docker
- Docker Compose
- Jenkins (for CI/CD automation)

---

## Learning Outcome

Through this project, I practiced:

- Jenkins pipeline automation
- Docker containerization
- CI/CD pipeline implementation
- Automated testing with Python
- Docker image build and push workflows
