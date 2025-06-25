
#
# BGP session poc
# --------------
#
# Makefile for project tasks
#

up:
	docker-compose  up

migrate:
	./bin/sandbox makemigrations core
	./bin/sandbox makemigrations
	./bin/sandbox migrate core
	./bin/sandbox migrate
