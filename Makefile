install: #install poetry
	poetry install

build: #run build package
	poetry build

package-install: #install package
	python3 -m pip uninstall dist/*.whl
	python3 -m pip install --user dist/*.whl

lint: #linter for code
	poetry run flake8 --ignore=F401 gendiff tests

test-package: #test package without install
	poetry run python3 -m gendiff.scripts.script_gendiff -f json ./tests/fixtures/file1.json ./tests/fixtures/file2.json

update: #update dependencies
	poetry update --lock

test: #start pytest
	poetry run pytest -vv

coverage: #start pytest code coverage
	poetry run pytest --cov gendiff --cov-report xml

test-func: #test function
	poetry run python3 -m gendiff.gendiff
