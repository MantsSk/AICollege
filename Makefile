.PHONY: install migrate seed dev css css-watch

install:
	pip install -r requirements-local.txt

migrate:
	alembic upgrade head

seed:
	python -m app.seed

css:
	./scripts/build-css.sh

css-watch:
	./scripts/build-css.sh --watch

dev: css migrate seed
	uvicorn app.main:app --reload --port 8000
