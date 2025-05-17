#!/bin/bash

PROJECT_BASE_DIR=test_manager
SONARQUBE_URL=http://localhost:9000
SONARQUBE_PROJECT_KEY=fastapi-sonarqube
SONARQUBE_TOKEN=sqp_319836e0c8adee09481c497803d4ebcf26b522e8

docker run \
		--network=host \
		-v $PWD:/$PROJECT_BASE_DIR \
		-e SONAR_HOST_URL="$SONARQUBE_URL" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$SONARQUBE_PROJECT_KEY -Dsonar.login=$SONARQUBE_TOKEN -Dsonar.projectBaseDir=/$PROJECT_BASE_DIR" \
		sonarsource/sonar-scanner-cli	

