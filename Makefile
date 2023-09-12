include .env
	
build-all:
	sudo ${DOCKER_COMPOSE} up --build -d --force-recreate

build-web:
	sudo ${DOCKER_COMPOSE} up --build -d --force-recreate web

restart-web:
	sudo ${DOCKER_COMPOSE} restart web

stop:
	sudo ${DOCKER_COMPOSE} stop

logs:
	sudo ${DOCKER_COMPOSE} logs -f

logs-web:
	sudo ${DOCKER_COMPOSE} logs -f web

logs-redis:
	sudo ${DOCKER_COMPOSE} logs -f redis

logs-db:
	sudo ${DOCKER_COMPOSE} logs -f db

logs-scheduler:
	sudo ${DOCKER_COMPOSE} logs -f scheduler

psql:
	sudo ${DOCKER_COMPOSE} exec db psql -U ${POSTGRES_USER}

makemigrations:
	sudo ${DOCKER_COMPOSE} exec web alembic revision --autogenerate

migrate:
	sudo ${DOCKER_COMPOSE} exec web alembic upgrade head

shell:
	sudo ${DOCKER_COMPOSE} exec web python -m ptpython

init-db:
	sudo ${DOCKER_COMPOSE} exec web python app/db/init_db.py

init-test-db:
	sudo ${DOCKER_COMPOSE} -f test.yml exec web python app/db/init_db.py

test:
	sudo ${DOCKER_COMPOSE} -f test.yml up --build --abort-on-container-exit --force-recreate

entrypoint:
	sudo ${DOCKER_COMPOSE} exec web bash ./entrypoint.sh

init-build: build-all entrypoint makemigrations migrate init-db
