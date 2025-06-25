
#
# BGP session poc
# --------------
#
# Makefile for project tasks
#

pip_setup:
	test -d env || python -m venv env
	. env/bin/activate
	pip install -r requirements.txt

up:
	docker-compose  up

migrate: pip_setup
	python manage.py makemigrations
	python manage.py migrate
