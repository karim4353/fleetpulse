.PHONY: up down build test demo lint

up:
	docker-compose up --build -d

down:
	docker-compose down -v

build:
	docker-compose build --no-cache

test:
	pytest -q

demo:
	bash scripts/demo.sh
