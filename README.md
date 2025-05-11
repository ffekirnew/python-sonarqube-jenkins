# python-sonarqube-jenkins

A template and demonstration project for integrating SonarQube and Jenkins with a FastAPI Python application, providing a robust CI/CD pipeline and automated code quality analysis.

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

This repository demonstrates how to build a modern CI/CD pipeline using **SonarQube** for code quality and **Jenkins** for automation, integrated with a sample **FastAPI** application. It includes ready-to-use Docker Compose files, Makefile commands, and scripts for both local and cloud deployment.

## Features

- **FastAPI Task Manager**: REST API for task management (CRUD).
- **SonarQube Integration**: Automated code quality and coverage checks.
- **Jenkins Integration**: Automated CI/CD pipeline.
- **Dockerized Setup**: Simple local deployment for SonarQube and Jenkins.
- **Cloud Ready**: GCP deployment instructions included.
- **Comprehensive Testing**: Unit tests and coverage reports.

## Architecture

```
[Developer] → [Git Repo] → [Jenkins] → [SonarQube] → [FastAPI App]
```

- **Jenkins**: Automates testing and triggers SonarQube analysis.
- **SonarQube**: Analyzes code quality and test coverage.
- **FastAPI**: Target application for CI/CD and code analysis.

## Directory Structure

```
sonarqube-fastapi/         # FastAPI app and scripts
  ├── task_manager/        # FastAPI source code and tests
  ├── Makefile             # Automation commands
  ├── run_sonarqube.sh     # SonarQube analysis script
  ├── sonar-project.properties # SonarQube config
jenkins/                  # Jenkins Docker Compose setup
sonarqube/                # SonarQube Docker Compose setup
```

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/)
- Docker & Docker Compose
- Make (optional)

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
  - `GET /tasks/{task_id}` - Retrieve a task
  - `PUT /tasks/{task_id}` - Update a task
  - `DELETE /tasks/{task_id}` - Delete a task

### SonarQube Analysis

- **Configure:** Edit `sonar-project.properties` as needed.
- **Run Analysis:**
  ```sh
  ./run_sonarqube.sh
  # or
  make sonarqube.scan.docker
  ```
- **View Results:**
  Visit [http://localhost:9000](http://localhost:9000) to view code quality reports.

### Jenkins CI/CD

- **Configure Jenkins:**
  - Install required plugins: SonarQube Scanner, Pipeline, etc.
  - Set up a pipeline to run tests and SonarQube analysis.
  - Connect to your Git repository.

## Testing

- **Run unit tests:**
  ```sh
  make test.run
  # or
  poetry run pytest task_manager
  ```
- **Generate coverage report:**
  ```sh
  make test.coverage.report
  ```

## Configuration

- **SonarQube:** `sonar-project.properties`
- **Jenkins:** `jenkins/docker-compose.yml`
- **FastAPI:** `sonarqube-fastapi/task_manager/src/`

## Cloud Deployment

- For step-by-step GCP deployment, see [documentation/demo.md](documentation/demo.md).

---

For a detailed walkthrough, refer to [documentation/demo.md](documentation/demo.md).
