# Jenkins CI/CD Pipeline with Docker Agent — URL Health Monitor

This project demonstrates a **complete CI/CD pipeline using Jenkins Docker Agent** where a
Docker container spins up as a build agent, runs the pipeline, and is destroyed after the job.
The application is a **URL Health Monitor** that checks whether a list of URLs are UP or DOWN
along with their response time and status code.

---

## Overview

The goal of this project is to demonstrate a **Docker Agent workflow** with the following steps:

- Build a custom Docker image to use as a Jenkins Agent
- Agent container spins up automatically when pipeline starts
- All build workloads run inside the container, never on Jenkins Master
- Build and test a Python URL Health Monitor application inside the container
- Containerize the application using Docker
- Push the Docker image to Docker Hub from the container
- Automate the entire pipeline using Jenkins
- Agent container destroyed automatically after job completes

The application itself is a **URL Health Monitor utility** that reads a list of URLs from a
JSON config file, checks each URL for availability, and reports the status, HTTP status code,
and response time in milliseconds. Unit tests are included using Python's `unittest` framework
to validate the core monitoring logic.

---

## Architecture
```
GitHub Push
     ↓
Jenkins Master (Azure VM)
     ↓ spins up Docker container as agent
Docker Agent Container ← created per pipeline run
     ↓
Checkout → Test → Docker Build → Push to DockerHub
     ↓
Container destroyed after job ✅
```

---

## Project Structure
```
02-docker-agent/
│
├── app/
│   ├── monitor.py
│   └── urls.json
│
├── tests/
│   ├── __init__.py
│   └── test_monitor.py
│
├── requirements.txt
├── Dockerfile
├── agent.Dockerfile
├── Jenkinsfile
└── README.md
```

### Files Description

| File | Purpose |
|------|---------|
| `app/monitor.py` | Core URL health check logic |
| `app/urls.json` | List of URLs to monitor |
| `tests/test_monitor.py` | Unit tests for the monitor |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Defines the application Docker image |
| `agent.Dockerfile` | Defines the Jenkins Docker Agent image |
| `Jenkinsfile` | Jenkins CI/CD pipeline configuration |

---

## Sample Output
```
Checking URLs...

https://google.com     → UP   | 200 | 112ms
https://github.com     → UP   | 200 | 234ms
https://fakeurl.xyz    → DOWN | --- | timeout
```

---

## Running the Application Locally

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the monitor:
```bash
python app/monitor.py
```

---

## Running Tests
```bash
python -m unittest discover tests
```

---

## Running with Docker

Build Docker image:
```bash
docker build -t url-health-monitor .
```

Run container:
```bash
docker run url-health-monitor
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout** – Pull code from GitHub into the Docker Agent container
2. **Install Dependencies** – Install Python packages inside container
3. **Build** – Run the URL Health Monitor inside container
4. **Test** – Run Python unit tests inside container
5. **Docker Build** – Build application Docker image inside container
6. **Docker Push** – Push image to DockerHub from container

Pipeline defined in `Jenkinsfile`.

---

## Docker Agent Setup Steps

1. Build the agent image using `agent.Dockerfile`
2. Push agent image to DockerHub
3. Jenkins Master pulls agent image when pipeline triggers
4. Container spins up → pipeline runs → container destroyed
5. Jenkinsfile uses `agent { docker { image '...' } }` to target container

---

## Static Agent vs Docker Agent

| | Static Agent | Docker Agent |
|---|---|---|
| VM needed | Yes — always running | No — container only |
| Cost | Always paying | Pay only during build |
| Clean environment | No — state builds up | Yes — fresh every build |
| Setup effort | Manual VM + Java | Just a Dockerfile |
| Startup time | Instant | Seconds |

---

## Prerequisites

- Docker
- Jenkins (with Docker Pipeline plugin)
- Azure Account (for Jenkins Master VM)
- DockerHub Account

---

## Learning Outcome

Through this project, I practiced:

- Jenkins Docker Agent architecture
- Building custom Docker agent images
- Ephemeral agent concept — spin up, build, destroy
- Isolating build environments using containers
- Docker socket mounting for Docker-in-Docker builds
- CI/CD pipeline automation with Jenkins
- Pushing Docker images to DockerHub through Jenkins
- Understanding Docker Agent advantages over Static Agents

---

## Author
Nagabhushanam Meka
DevOps Engineer | github.com/BhushanGit04096
