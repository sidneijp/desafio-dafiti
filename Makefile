SHELL:=/bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
BASE_PATH=${PWD}
PYTHON_EXEC=pipenv run

include .env
export $(shell sed 's/=.*//' .env)

list:
	sh -c "echo; $(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'Makefile'| sort"

#############################
# Docker machine states
#############################

_cp_env_file:
	cp -f .env.sample .env
	echo "" >> .env
	echo "DOCKER_USER=`whoami`" >> .env
	echo "DOCKER_USER_ID=`id -u ${DOCKER_USER}`" >> .env
	echo "DOCKER_GROUP=`whoami`" >> .env
	echo "DOCKER_GROUP_ID=`id -g ${DOCKER_GROUP}`" >> .env

_migrate:
	docker-compose run --rm web python manage.py migrate

_build:
	docker-compose build

_rebuild:
	docker-compose down
	docker-compose build --no-cache

init: _cp_env_file _rebuild _migrate

up:
	docker-compose build --force-rm
	docker-compose up -d --remove-orphans

start:
	docker-compose start ${ARGS}

restart:
	docker-compose restart ${ARGS}

stop:
	docker-compose stop ${ARGS}

down:
	docker-compose down

status:
	docker-compose ps

logs:
	docker-compose logs -f ${ARGS}

install:
	docker-compose exec web pipenv install ${ARGS}

sh:
	docker-compose exec ${ARGS} ash

dj:
	docker-compose exec web ${PYTHON_EXEC} ./manage.py ${ARGS}

test:
	docker-compose exec web ${PYTHON_EXEC} py.test ${ARGS}

test-watch:
	docker-compose exec web ${PYTHON_EXEC} ptw ${ARGS}

coverage:
	docker-compose exec web ${PYTHON_EXEC} pytest --cov=. ${ARGS}

report:
	docker-compose exec web ${PYTHON_EXEC} coverage report ${ARGS}

html:
	docker-compose exec web ${PYTHON_EXEC} coverage html ${ARGS}

_drop_db:
	docker-compose stop db
	docker-compose rm db

_create_db:
	docker-compose up -d db

recreate_db: _drop_db _create_db

python_path:
	echo "`docker-compose exec web pipenv --venv`"

# Front stuff

yarn:
	docker-compose run --rm front "yarn" ${ARGS}

_generates_fake_data:
	docker-compose run --rm web python manage.py generates_fake_data

#############################
# Argument fix workaround
#############################
%:
	@:

