.PHONY: help install dev test clean deploy docker-build docker-run

# Variables
PYTHON := python3
PIP := pip3
STAGE := preprod

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install: ## Install dependencies
	$(PIP) install -r requirements.txt

install-dev: ## Install development dependencies
	$(PIP) install -r requirements.txt
	$(PIP) install pytest pytest-cov black flake8 mypy

dev: ## Run development server
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

test: ## Run tests
	pytest src/tests/ -v --cov=src --cov-report=term-missing

test-watch: ## Run tests in watch mode
	pytest-watch src/tests/ -v

format: ## Format code with black
	black src/

lint: ## Lint code with flake8
	flake8 src/ --max-line-length=100 --exclude=__pycache__,venv

type-check: ## Type check with mypy
	mypy src/

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf .serverless
	rm -f test.db

db-migrate: ## Create new migration
	alembic revision --autogenerate -m "$(MSG)"

db-upgrade: ## Apply migrations
	alembic upgrade head

db-downgrade: ## Rollback one migration
	alembic downgrade -1

# Docker commands
docker-build: ## Build Docker image
	docker build -t parking-management-api .

docker-run: ## Run Docker container
	docker run -p 8000:8000 --env-file .env parking-management-api

docker-compose-up: ## Start services with docker-compose
	docker-compose up -d

docker-compose-down: ## Stop services
	docker-compose down

# Serverless commands
sls-install: ## Install Serverless dependencies
	npm install

sls-deploy: ## Deploy to AWS
	serverless deploy --stage $(STAGE)

sls-deploy-dev: ## Deploy to dev stage
	serverless deploy --stage dev

sls-deploy-prod: ## Deploy to prod stage
	serverless deploy --stage prod

sls-logs: ## Tail serverless logs
	serverless logs -f api --stage $(STAGE) --tail

sls-remove: ## Remove serverless deployment
	serverless remove --stage $(STAGE)

sls-offline: ## Run serverless offline
	serverless offline --stage dev

# Database seeding
seed-db: ## Seed database with sample data
	$(PYTHON) scripts/seed_database.py

# Full setup
setup: install sls-install ## Full project setup
	@echo "Setup complete!"

# CI/CD
ci-test: ## Run tests for CI
	pytest src/tests/ -v --cov=src --cov-report=xml

ci-deploy: ## Deploy from CI
	serverless deploy --stage $(STAGE) --verbose