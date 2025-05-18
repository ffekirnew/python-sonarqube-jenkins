# Introduction

This demo will guide you through setting up a robust CI/CD pipeline using SonarQube and Jenkins, integrated with a FastAPI application. By the end of this demo, you will have a clear understanding of how to analyze code quality and automate deployments.

# What this demo will cover:

- Setting up SonarQube for code quality analysis.

- Integrating SonarQube with a FastAPI application.

- Running code analysis using `sonar-scanner`.

- Setting up Jenkins for CI/CD.

- Deploying SonarQube and Jenkins on Google Cloud Platform (GCP).

# SonarQube setup

1. **Install SonarQube**: Use the provided `docker-compose.yml` file in the `sonarqube` directory to set up SonarQube locally.

2. **Start the SonarQube services**: Use the following command to start SonarQube and its dependencies:
   ```bash
   make sonarqube.start
   ```

3. **Configure SonarQube**: Access the SonarQube dashboard at `http://localhost:9000` and create a new project.

4. **Generate a Token**: Use the token to authenticate the SonarQube scanner .

# FastAPI Application

1. **Overview**: The FastAPI application is located in the `sonarqube-fastapi` directory. It includes a task management system.

2. **Dependencies**: Install dependencies using Poetry (`poetry install`).
    ```bash
    cd sonarqube-fastapi
    poetry install
    ```

3. **Testing**: Run unit tests located in `task_manager/tests/unit_tests` to ensure the application is functioning correctly.
    ```bash
    make test
    ```

    Or alternatively, you can run the tests using the following command:
    ```bash
    make test.coverage.report
    ```

# Running analysis with SonarQube | Sonar-project.properties

1. **Configuration**: The `sonar-project.properties` file contains the configuration for the SonarQube scanner.
   - Key properties include `sonar.projectKey`, `sonar.sources`, and `sonar.host.url`.

2. **Run Analysis**: Use the `run_sonarqube.sh` script or the `Makefile` commands to execute the analysis.
   ```bash
   ./run_sonarqube.sh
   ```

   Alternatively, you can use the following Makefile command to run the SonarScanner in Docker:
   ```bash
   make sonarqube.scan.docker
   ```

3. **View Results**: Check the SonarQube dashboard for analysis results and code quality metrics.

# Jenkins Setup

1. **Install Jenkins**: Use the `docker-compose.yml` file in the `jenkins` directory to set up Jenkins locally.

2. **Start the Jenkins services**: Use the following command to start Jenkins and its dependencies:
   ```bash
   make jenkins.start
   ```

2. **Configure Jenkins**:
   - Install necessary plugins (e.g., SonarQube Scanner, Pipeline).
   - Set up a pipeline to automate code analysis and deployment.

3. **Integrate with SonarQube**: Add SonarQube as a tool in Jenkins and configure the pipeline to run SonarQube analysis.

# Next Steps:

1. **Cloud Deployment**:
   - Transition from local development to cloud-based solutions for scalability and reliability.
   - Use Google Cloud Platform (GCP) to host SonarQube and Jenkins.

2. **CI/CD Pipeline Enhancement**:
   - Integrate Jenkins with cloud-based repositories like GitHub or GitLab.
   - Automate the deployment process to cloud environments using Jenkins pipelines.

3. **Monitoring and Logging**:
   - Set up monitoring tools like Prometheus and Grafana to track the performance of SonarQube and Jenkins.
   - Use centralized logging solutions like ELK Stack (Elasticsearch, Logstash, and Kibana) for better debugging and analysis.

4. **Security Improvements**:
   - Implement secure access controls for SonarQube and Jenkins.
   - Use SSL/TLS certificates to encrypt communication.

5. **Scaling**:
   - Explore container orchestration tools like Kubernetes to manage and scale SonarQube and Jenkins deployments.
   - Use auto-scaling features to handle increased workloads efficiently.

# Deploying SonarQube on GCP

1. **Create a VM**: Use Google Cloud Console to create a virtual machine.

2. **Install Docker**: Set up Docker on the VM.

3. **Deploy SonarQube**: Use the `docker-compose.yml` file to deploy SonarQube on the VM.

# Deploying Jenkins on GCP

1. **Create a VM**: Use Google Cloud Console to create a virtual machine.

2. **Install Docker**: Set up Docker on the VM.

3. **Deploy Jenkins**: Use the `docker-compose.yml` file to deploy Jenkins on the VM.

