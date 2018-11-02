.DEFAULT_GOAL := dev

%.built: % dockerfiles/Dockerfile.base dockerfiles/Dockerfile.warning
	cat dockerfiles/Dockerfile.warning > $@
	cat dockerfiles/Dockerfile.base >> $@
	cat $< >> $@

prod: dockerfiles/Dockerfile.prod.built
	docker build -t sour:prod -f dockerfiles/Dockerfile.prod.built .

dev: dockerfiles/Dockerfile.dev.built
	docker build -t sour:dev -f dockerfiles/Dockerfile.dev.built .

server: dockerfiles/Dockerfile.server.built
	docker build -t sour:server -f dockerfiles/Dockerfile.server server/

clean:
	find dockerfiles/ -name "*.built" -delete
	docker rmi sour:dev
	rm *.built
	rm -r dist build *.egg-info
