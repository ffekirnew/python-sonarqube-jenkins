include .env

.PHONY: init_swarm leave_swarm sonarqube.start sonarqube.stop sonarqube.scan sonarqube.scan.docker sonarqube.scan.docker.log jenkins.start fastapi.run test.run test.coverage test.coverage.report activate_venv
PROJECT_BASE_DIR=task_manager

init_swarm:
	@echo "Initializing Docker Swarm..."
	@docker swarm init || echo "Swarm already initialized"
	@docker network create --driver overlay --attachable sonar_network || echo "Network already exists"

leave_swarm:
	@echo "Leaving swarm..."
	@docker swarm leave --force

sonarqube.start: init_swarm
	@echo "Deploying SonarQube stack..."
	@docker stack deploy -c ../sonarqube/docker-compose.yml sonar

sonarqube.stop:
	@echo "Stopping SonarQube stack..."
	@docker stack rm sonar

jenkins.start: init_swarm
	@echo "Deploying Jenkins stack..."
	@docker stack deploy -c ../jenkins/docker-compose.yml jenkins

jenkins.stop:
	@echo "Stopping Jenkins stack..."
	@docker stack rm jenkins

fastapi.run:
	@echo "Running FastAPI..."
	@fastapi dev task_manager/src/main.py

test.docker.build:
	@echo "Building Docker image for tests..."
	@docker build -t fastapi-test -f Dockerfile.test .

test.docker.run: test.docker.build
	@echo "Running tests in Docker..."
	@docker run --rm fastapi-test

test.run:
	@echo "Running tests..."
	@python -m pytest $(PROJECT_BASE_DIR)

test.coverage:
	@echo "Running tests with coverage..."
	@python -m pytest --cov=src --cov-report=term-missing $(PROJECT_BASE_DIR)

test.coverage.report:
	@echo "Generating coverage report..."
	@python -m pytest --cov-report xml:coverage.xml --cov=src --junitxml=result.xml $(PROJECT_BASE_DIR)

sonarqube.scan.docker:
	@echo "Running SonarScanner in Docker..."
	@docker run \
		--network=host \
		-v $(PWD):/$(PROJECT_BASE_DIR) \
		-e SONAR_HOST_URL="$(SONARQUBE_URL)" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY) -Dsonar.login=$(SONARQUBE_TOKEN) -Dsonar.projectBaseDir=/$(PROJECT_BASE_DIR)" \
		sonarsource/sonar-scanner-cli

sonarqube.scan.docker.log:
	@echo "Running SonarScanner in Docker..."
	@docker run \
		--network=host \
		-v $(PWD):/$(PROJECT_BASE_DIR) \
		-e SONAR_HOST_URL="$(SONARQUBE_URL)" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY) -Dsonar.login=$(SONARQUBE_TOKEN) -Dsonar.projectBaseDir=/$(PROJECT_BASE_DIR)" \
		sonarsource/sonar-scanner-cli	-X

activate_venv:
	@echo "Activating virtual environment..."
	@source /Users/ffekirnew/Library/Caches/pypoetry/virtualenvs/python-sonarqube-jenkins-jxBsoVsh-py3.13/bin/activate
