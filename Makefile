
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
	@rm -rf flask-backend/database.sqlite3;

.PHONY: run
run:
	@cd react-frontend/; \
	npm run build; \
	cd ../flask-backend; \
	python3 main.py; \

.PHONY: all
all: install run
