
start:
	poetry run gunicorn go_fastapi.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80

test: unit-tests

unit-tests:
	pytest tests/unit/*.py
