run:
	uvicorn sandbox.asgi:application --reload

format:
	isort --profile black .
	black .
