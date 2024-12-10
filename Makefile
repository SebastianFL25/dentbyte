build:
	docker-compose build

up:
	docker-compose up -d

server:
	docker-compose up db_posgres web

shell-server:
	docker-compose exec web bash

shell-mysql:
	docker-compose exec db_posgres bash
