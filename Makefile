install:
	poetry install

dev:
	poetry run flask --app zluuba_art:app --debug run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) zluuba_art:app

linter:
	poetry run flake8 zluuba_art

typing:
	poetry run mypy --install-types
	poetry run mypy zluuba_art

full-check:
	make linter
	make typing
