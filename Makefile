run:
	uvicorn sandbox.asgi:application --reload

test:
	pytest -vv --cov=sandbox --cov-report=term-missing

format:
	isort --profile=black .
	black .

lint-isort:
	isort --profile=black --check .

lint-black:
	black --check .

lint: lint-isort lint-black

build:
	docker image build -t sandbox .

up:
	docker-compose up --detach --build --remove-orphans

down:
	docker-compose down
