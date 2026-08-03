run:
	uvicorn api.app:app --reload

test:
	pytest

lint:
	python -m compileall .

format:
	python -m black .
