
.PHONY: venv
venv:
	@python3 -m venv venv;
	@echo "Type \"source venv/bin/activate\" in your command line to \
	activate the virtual environment"

.PHONY: install
install:
	@pip install --upgrade pip; \
	pip install poetry==0.12.17; \
	poetry install; \
	cd client/; \
	npm install; \

.PHONY: clean
clean:
	@rm -rf .mypy_cache/;
	@rm -rf .tox/;
	@rm -rf re.are.na.egg-info/;
	@rm -rf database.sqlite3;
	@rm -rf server/database.sqlite3;
	@rm -rf server/pkg/database.sqlite3;
	@rm -rf server/tests/database.sqlite3;
	@rm -rf server/__pycache__/;
	@rm -rf server/pkg/__pycache__/;
	@rm -rf server/pkg/html/__pycache__/;
	@rm -rf server/tests/__pycache__/;
	@rm -rf server/tests/snapshots/__pycache__/;
	@rm -rf .pytest_cache/;

.PHONY: flask
flask:
	@cd server; \
	poetry run python3 main.py; \

.PHONY: react
react:
	@cd client/; \
	yarn start; \

.PHONY: email
email:
	@cd server; \
	python3 main.py --email; \
