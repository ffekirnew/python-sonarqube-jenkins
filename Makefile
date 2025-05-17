include .env

.PHONY: init_swarm run_sonarqube stop_sonarqube leave_swarm

# Initialize swarm and create network
init_swarm:
	@echo "Initializing Docker Swarm..."
	@docker swarm init || echo "Swarm already initialized"
	@docker network create --driver overlay --attachable sonar_network || echo "Network already exists"

# Optional: Leave the swarm (force = OK for single-node)
leave_swarm:
	@echo "Leaving swarm..."
	@docker swarm leave --force

# Deploy the SonarQube stack
sonarqube.start: init_swarm
	@echo "Deploying SonarQube stack..."
	@docker stack deploy -c sonarqube/docker-compose.yml sonar

# Optional: Stop and remove the SonarQube stack
sonarqube.stop:
	@echo "Stopping SonarQube stack..."
	@docker stack rm sonar

# Run SonnarScanner
sonarqube.scan:
	@echo "Running SonarScanner..."
	@sonar-scanner \
  -Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY) \
  -Dsonar.sources=. \
  -Dsonar.host.url=$(SONARQUBE_URL) \
  -Dsonar.login=$(SONARQUBE_TOKEN)

sonarqube.scan.docker:
	@docker run \
		--network=host \
    -e SONAR_HOST_URL="$(SONARQUBE_URL)" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY)" \
    -e SONAR_LOGIN=$(SONARQUBE_TOKEN) \
    -v "$(SONARQUBE_REPO):/src" \
    sonarsource/sonar-scanner-cli	

sonarqube.scan.docker.log:
	@docker run \
		--rm \
		--network=host \
    -e SONAR_HOST_URL="$(SONARQUBE_URL)" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY)" \
    -e SONAR_LOGIN=$(SONARQUBE_TOKEN) \
    -v "$(SONARQUBE_REPO):/src" \
    sonarsource/sonar-scanner-cli	-X

fastapi.run:
	@echo "Running FastAPI..."
	@fastapi dev src/main.py

test.run:
	@echo "Running tests..."
	@python -m pytest .

test.coverage:
	@echo "Running tests with coverage..."
	@python -m pytest --cov=src --cov-report=term-missing .

test.coverage.report:
	@echo "Generating coverage report..."
	@python -m pytest --cov-report xml:coverage.xml --cov=src --junitxml=result.xml .
