dev:
	poetry run flask --app zluuba_art:app --debug run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) zluuba_art:app

install:
	poetry install

lint:
	poetry run flake8 zluuba_art

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_analyzer --cov-report xml
