# Jenkins CI/CD Pipeline for a Dockerized Python Log Analyzer

This project demonstrates a **complete CI/CD pipeline using Jenkins, Docker, and Docker Compose** for a Python-based log analyzer utility. It shows how source code can be automatically built, tested, containerized, and deployed using Jenkins.

---

## Overview

The goal of this project is to demonstrate a basic **CI/CD workflow** with the following steps:

- Build and test a Python application
- Containerize the application using Docker
- Run the container using Docker Compose
- Automate the pipeline using Jenkins
- Push the Docker image to Docker Hub

The application itself is a small **log analysis utility** that scans log data and counts the number of **ERROR entries**. A unit test is included using Python's `unittest` framework to validate the functionality.

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
| `app.py` | Python log analyzer script |
| `tests/test_app.py` | Unit tests for the log analyzer |
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
Total ERROR entries found: 2
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
docker build -t python-jenkins-log-analyzer .
```

Run container:

```bash
docker run python-jenkins-log-analyzer
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
- Building and pushing Docker images through Jenkins
- Basic log analysis automation using Python
