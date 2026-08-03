run:
	uvicorn api.app:app --reload

test:
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -v

lint:
	python -m compileall .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
