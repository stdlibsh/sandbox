run:
	uvicorn sandbox.asgi:application --reload

format:
	isort --profile black .
	black .

build:
	docker image build -t sandbox .

up:
	docker-compose up --detach --build --remove-orphans

down:
	docker-compose down
