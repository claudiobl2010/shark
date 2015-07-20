start:
	@python src/shark/app/wsgi.py

gunicorn:
	@gunicorn -b 0.0.0.0:5000 --chdir src shark.app.wsgi:app
