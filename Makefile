.PHONY: install
install: # install the poetry project package itself plus its dependencies.
	poetry install


.PHONY: start
start: # start the service
	poetry run python src/main.py