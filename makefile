docker-up-dev:
	docker-compose -f docker-compose.dev.yml up

docker-up-rebuild-dev:
	docker-compose -f docker-compose.dev.yml up --force-recreate --build

docker-rebuild-dev:
	docker-compose -f docker-compose.dev.yml build --no-cache $(resource)

docker-restart-component:
	docker restart $(resource)