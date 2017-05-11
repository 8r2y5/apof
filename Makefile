RUN = docker-compose run --rm

.PHONY: all

all: stop js_build collectstatic migrate up build deploy

SHELL := /bin/bash

stop:
	docker-compose stop

js_build:
	$(RUN) fron

collectstatic: | js_build
	$(RUN) web django collectstatic --noinput

migrate:
	$(RUN) web django migrate

up:
	docker-compose up -d

build:
	docker-compose build

reload: | stop up

deploy: | stop collectstatic migrate up

default: deploy
