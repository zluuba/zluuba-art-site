install:
	poetry install

dev:
	poetry run flask --app zluuba_art:app --debug run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) zluuba_art:app
