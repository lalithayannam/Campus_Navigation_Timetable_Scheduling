install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest --cov=app --cov-report=term-missing

quality:
	ruff check .
	black --check .
	mypy app

format:
	black .
	ruff check . --fix
