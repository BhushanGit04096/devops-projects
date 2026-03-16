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
