# Jenkins CI/CD Pipeline with Static Agent — URL Health Monitor

This project demonstrates a **complete CI/CD pipeline using Jenkins Static Agent** where a
permanent Azure VM acts as a dedicated build agent. The application is a **URL Health Monitor**
that checks whether a list of URLs are UP or DOWN along with their response time and status code.

---

## Overview

The goal of this project is to demonstrate a **Static Agent workflow** with the following steps:

- Set up a permanent Jenkins Agent VM connected to Jenkins Master via SSH
- Assign all build workloads to the Agent, never the Master
- Build and test a Python URL Health Monitor application on the Agent
- Containerize the application using Docker on the Agent
- Push the Docker image to Docker Hub from the Agent
- Automate the entire pipeline using Jenkins

The application itself is a **URL Health Monitor utility** that reads a list of URLs from a
JSON config file, checks each URL for availability, and reports the status, HTTP status code,
and response time in milliseconds. Unit tests are included using Python's `unittest` framework
to validate the core monitoring logic.

---

## Architecture
```
GitHub Push
     ↓
Jenkins Master (Azure VM 1)
     ↓ assigns job via SSH
Static Agent (Azure VM 2) ← permanently connected
     ↓
Checkout → Test → Docker Build → Push to DockerHub
```

---

## Project Structure
```
01-static-agent/
│
├── app/
│   ├── monitor.py
│   └── urls.json
│
├── tests/
│   └── test_monitor.py
│
├── requirements.txt
├── Dockerfile
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
| `Dockerfile` | Defines the Docker image |
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

1. **Checkout** – Pull code from GitHub onto the Static Agent
2. **Test** – Run Python unit tests on the Agent
3. **Docker Build** – Build Docker image on the Agent
4. **Docker Push** – Push image to DockerHub from the Agent

Pipeline defined in `Jenkinsfile`.

---

## Static Agent Setup Steps

1. Create Agent VM on Azure (Ubuntu 22.04)
2. Install Java 17 on Agent VM
3. Add Agent credentials in Jenkins Master → Manage Jenkins → Nodes
4. Label the agent as `static-agent`
5. Verify Agent is online in Jenkins UI
6. Jenkinsfile uses `agent { label 'static-agent' }` to target this Agent VM

---

## Prerequisites

- Python 3.x
- Docker
- Java 17 (on Agent VM — required for Jenkins agent process)
- Jenkins (Master VM for CI/CD automation)
- Azure Account (for VM provisioning)

---

## Learning Outcome

Through this project, I practiced:

- Jenkins Master and Agent architecture
- Permanent Static Agent setup and connection via SSH
- Isolating build workloads away from Jenkins Master
- Real-world URL health monitoring with Python
- Docker containerization on a dedicated Agent VM
- CI/CD pipeline automation with Jenkins
- Pushing Docker images to DockerHub through Jenkins
- Understanding Static Agent limitations vs Dynamic Agents

---

## Author
Nagabhushanam Meka
DevOps Engineer | github.com/BhushanGit04096
```

---

Only change from before:
```
tests/ is now separate folder ✅
unittest discover tests  ✅
