# Jenkins CI/CD Pipeline with Kubernetes Agent — URL Health Monitor

This project demonstrates a **complete CI/CD pipeline using Jenkins Kubernetes Agent** where a
Kubernetes Pod spins up as a build agent, runs the pipeline, and is destroyed after the job.
The application is a **URL Health Monitor** that checks whether a list of URLs are UP or DOWN
along with their response time and status code.

---

## Overview

The goal of this project is to demonstrate a **Kubernetes Agent workflow** with the following steps:

- Set up a GKE (Google Kubernetes Engine) cluster on GCP
- Install Jenkins Kubernetes plugin
- Configure Jenkins to connect to GKE cluster
- Pod spins up automatically when pipeline starts
- All build workloads run inside the Pod, never on Jenkins Master
- Build and test a Python URL Health Monitor application inside the Pod
- Containerize the application using Docker
- Push the Docker image to Docker Hub from the Pod
- Automate the entire pipeline using Jenkins
- Pod destroyed automatically after job completes

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
     ↓ creates Pod in GKE cluster
Kubernetes Pod ← created per pipeline run
     ↓
Checkout → Test → Docker Build → Push to DockerHub
     ↓
Pod destroyed after job ✅
GKE auto-scales if needed ✅
```

---

## Project Structure
```
03-kubernetes-agent/
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
├── pod-template.yaml
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
| `pod-template.yaml` | Kubernetes Pod template for Jenkins agent |
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

## GKE Cluster Setup Steps

### Step 1 — Set GCP Project
```bash
gcloud config set project <YOUR_PROJECT_ID>
```

### Step 2 — Enable GKE API
```bash
gcloud services enable container.googleapis.com
```

### Step 3 — Create GKE Cluster
```bash
gcloud container clusters create jenkins-k8s-cluster \
    --zone us-central1-a \
    --num-nodes 1 \
    --machine-type e2-medium
```

### Step 4 — Get Cluster Credentials
```bash
gcloud container clusters get-credentials jenkins-k8s-cluster \
    --zone us-central1-a
```

### Step 5 — Verify Cluster Running
```bash
kubectl get nodes
```

### Step 6 — Install Jenkins Kubernetes Plugin
```
Manage Jenkins → Plugins → Available
Search: Kubernetes
Install: Kubernetes plugin
Restart Jenkins
```

### Step 7 — Configure Kubernetes Cloud in Jenkins
```
Manage Jenkins → Clouds → New Cloud
Type          : Kubernetes
Name          : kubernetes
K8s URL       : (GKE cluster URL)
Credentials   : (kubeconfig/service account)
Jenkins URL   : http://<MASTER_IP>:8080
```

### Step 8 — Run Pipeline
```
Jenkins reads Jenkinsfile
Sees: agent { kubernetes { } }
Creates Pod in GKE cluster
Pipeline runs inside Pod
Pod destroyed after job ✅
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout** – Pull code from GitHub into the Kubernetes Pod
2. **Install Dependencies** – Install Python packages inside Pod
3. **Build** – Run the URL Health Monitor inside Pod
4. **Test** – Run Python unit tests inside Pod
5. **Docker Build** – Build application Docker image inside Pod
6. **Docker Push** – Push image to DockerHub from Pod

Pipeline defined in `Jenkinsfile`.

---

## Agent Comparison

| | Static Agent | Docker Agent | Kubernetes Agent |
|---|---|---|---|
| Infrastructure | Permanent VM | Container on VM | Pod in K8s cluster |
| Cost | Always paying | Low | Pay per build |
| Clean environment | No | Yes | Yes |
| Auto scaling | No | No | Yes ✅ |
| Setup effort | Easy | Medium | Complex |
| Best for | Small teams | Medium teams | Enterprise scale |

---

## Prerequisites

- Docker
- Jenkins with Kubernetes plugin
- GCP Account with GKE enabled
- kubectl installed
- DockerHub Account

---

## Learning Outcome

Through this project, I practiced:

- Jenkins Kubernetes Agent architecture
- GKE cluster creation and configuration on GCP
- Connecting Jenkins to Google Kubernetes Engine
- Ephemeral Pod agents — spin up, build, destroy
- Auto-scaling build infrastructure on GCP
- CI/CD pipeline automation with Jenkins
- Pushing Docker images to DockerHub through Jenkins
- Understanding Kubernetes Agent advantages over Docker/Static Agents

---

## Author
Nagabhushanam Meka
DevOps Engineer | github.com/BhushanGit04096
