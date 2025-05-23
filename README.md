# python-sonarqube-jenkins

A comprehensive template and demo for integrating SonarQube and Jenkins with a FastAPI Python application, enabling robust CI/CD pipelines and automated code quality analysis.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
- [Usage](#usage)
  - [FastAPI Task Manager](#fastapi-task-manager)
  - [SonarQube Analysis](#sonarqube-analysis)
  - [Jenkins CI/CD](#jenkins-cicd)
- [Testing](#testing)
- [Configuration](#configuration)
- [Cloud Deployment](#cloud-deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This project demonstrates how to set up a modern CI/CD pipeline using **SonarQube** for code quality analysis and **Jenkins** for automation, integrated with a sample **FastAPI** application. It provides ready-to-use Docker Compose files, Makefile commands, and scripts for local and cloud deployment.

## Features

- **FastAPI Task Manager**: Simple REST API for managing tasks (CRUD operations).
- **SonarQube Integration**: Automated code quality and coverage analysis.
- **Jenkins Integration**: CI/CD pipeline automation.
- **Dockerized Setup**: Easy local deployment for SonarQube and Jenkins.
- **Cloud Ready**: Instructions for deploying on Google Cloud Platform (GCP).
- **Comprehensive Testing**: Unit tests and coverage reporting.

## Architecture

```
[Developer] → [Git Repo] → [Jenkins] → [SonarQube] → [FastAPI App]
```

- **Jenkins** automates testing and triggers SonarQube analysis.
- **SonarQube** analyzes code quality and test coverage.
- **FastAPI** app is the target for CI/CD and code analysis.

## Directory Structure

```
sonarqube-fastapi/         # FastAPI app and related scripts
  ├── task_manager/        # Main FastAPI source code and tests
  ├── Makefile             # Automation commands
  ├── run_sonarqube.sh     # Script to run SonarQube analysis
  ├── sonar-project.properties # SonarQube config
jenkins/                  # Jenkins Docker Compose setup
sonarqube/                # SonarQube Docker Compose setup
```

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/)
- Docker & Docker Compose
- Make (optional, for convenience)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd python-sonarqube-jenkins
   ```
2. **Install FastAPI dependencies:**
   ```sh
   cd sonarqube-fastapi
   poetry install
   ```

### Running Locally

- **Start SonarQube:**
  ```sh
  make sonarqube.start
  # or
  docker-compose -f sonarqube/docker-compose.yml up -d
  ```
- **Start Jenkins:**
  ```sh
  make jenkins.start
  # or
  docker-compose -f jenkins/docker-compose.yml up -d
  ```
- **Run FastAPI app:**
  ```sh
  make fastapi.run
  # or
  poetry run uvicorn task_manager.src.main:Api --reload
  ```

## Usage

### FastAPI Task Manager

- **API Endpoints:**
  - `POST /tasks/` - Create a task
  - `GET /tasks/` - List all tasks
  - `GET /tasks/{task_id}` - Get a task
  - `PUT /tasks/{task_id}` - Update a task
  - `DELETE /tasks/{task_id}` - Delete a task

### SonarQube Analysis

- **Configure**: Edit `sonar-project.properties` as needed.
- **Run Analysis:**
  ```sh
  ./run_sonarqube.sh
  # or
  make sonarqube.scan.docker
  ```
- **View Results:**
  Visit [http://localhost:9000](http://localhost:9000) and log in to see code quality reports.

### Jenkins CI/CD

- **Configure Jenkins:**
  - Install plugins: SonarQube Scanner, Pipeline, etc.
  - Set up a pipeline to run tests and SonarQube analysis.
  - Integrate with your Git repository.

## Testing

- **Run unit tests:**
  ```sh
  make test.run
  # or
  poetry run pytest task_manager
  ```
- **Coverage report:**
  ```sh
  make test.coverage.report
  ```

## Configuration

- **SonarQube:** `sonar-project.properties`
- **Jenkins:** `jenkins/docker-compose.yml`
- **FastAPI:** `sonarqube-fastapi/task_manager/src/`

## Cloud Deployment

- See [documentation/demo.md](documentation/demo.md) for step-by-step instructions to deploy SonarQube and Jenkins on Google Cloud Platform (GCP).

---

For a detailed walkthrough, see [documentation/demo.md](documentation/demo.md).
