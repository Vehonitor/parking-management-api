all: install run

install:
	pip install -r requirements.txt

run:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest src/tests

migrate:
	alembic upgrade head

docker-build:
	docker build -t parking-management-api .

docker-run:
	docker run -p 8000:8000 parking-management-api

deploy:
	serverless deploy

.PHONY: install run test migrate docker-build docker-run deploy