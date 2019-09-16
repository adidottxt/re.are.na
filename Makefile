
.PHONY: venv
venv:
	@python3 -m venv venv;
	@echo "Type \"source venv/bin/activate\" in your command line to \
	activate the virtual environment"

.PHONY: install
install:
	@pip install --upgrade pip; \
	pip install -r requirements.txt; \
	cd react-frontend/; \
	npm install; \

.PHONY: clean
clean:
	@rm -rf .mypy_cache/;
	@rm -rf .tox/;
	@rm -rf re.are.na.egg-info/;
	@rm -rf database.sqlite3;
	@rm -rf flask-backend/database.sqlite3;
	@rm -rf flask-backend/pkg/__pycache__/;
	@rm -rf flask-backend/tests/database.sqlite3;
	@rm -rf flask-backend/tests/__pycache__/;
	@rm -rf .pytest_cache/;

.PHONY: flask
flask:
	@cd flask-backend; \
	python3 main.py; \

.PHONY: react
react:
	@cd react-frontend/; \
	yarn start; \
