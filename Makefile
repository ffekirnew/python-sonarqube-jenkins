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
	@docker stack deploy -c sonarqube/docker-compose.yml sonar

sonarqube.stop:
	@echo "Stopping SonarQube stack..."
	@docker stack rm sonar

jenkins.start: init_swarm
	@echo "Deploying Jenkins stack..."
	@docker stack deploy -c jenkins/docker-compose.yml jenkins

jenkins.stop:
	@echo "Stopping Jenkins stack..."
	@docker stack rm jenkins

jenkins.container:
	@docker run \
		--name jenkins \
		--detach \
		-v ./jenkins/data:/var/jenkins_home \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-p 8080:8080 \
		-p 50000:50000 \
		--restart=on-failure \
		ffekirnew/jenkins;
