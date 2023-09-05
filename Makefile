
up:
	sh scripts/devcontainer.sh up

down:
	sh scripts/devcontainer.sh down

dev:
	docker exec -it tmpagent /bin/bash

logs:
	docker logs -f tmpagent

restart:
	make down && make up
