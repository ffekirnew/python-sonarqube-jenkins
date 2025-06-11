#!/bin/bash

PROJECT_BASE_DIR=task_manager
SONARQUBE_URL=http://localhost:9000
SONARQUBE_PROJECT_KEY=fastapi-demo-2
SONARQUBE_TOKEN=sqp_dc6938d4e5794c6e8e21f69363d80960f5774836


docker run \
		--network=host \
		-v $PWD:/$PROJECT_BASE_DIR \
		-e SONAR_HOST_URL="$SONARQUBE_URL" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$SONARQUBE_PROJECT_KEY -Dsonar.login=$SONARQUBE_TOKEN -Dsonar.projectBaseDir=/$PROJECT_BASE_DIR" \
		sonarsource/sonar-scanner-cli	

