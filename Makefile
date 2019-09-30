.PHONY : clean test
.DEFAULT_GOAL := init

PACKAGE=parse_bom_stations

STATION_DOWNLOAD_FILE=tests/data/bomstations.zip
STATION_OUT_FILE = tests/data/bomstations.txt

export STATION_OUT_FILE

info:
	echo $(TMPDIR)
	echo $(STATION_DOWNLOAD_FILE)
	echo $(STATION_OUT_FILE)

init:
	pip install pipenv --upgrade
	pipenv install --dev
	pipenv run pre-commit install

check:
	pipenv check

lint:
	pipenv run pylint $(PACKAGE) tests bin

fetch-data:
	pipenv run python bin/fetch_bom_stations $(STATION_DOWNLOAD_FILE) $(STATION_OUT_FILE)

test: fetch-data
	pipenv run tox

pre-commit: lint check test

package:
	pipenv run python setup.py sdist bdist_wheel

clean:
	rm -rf build dist .egg .eggs *.egg-info pip-wheel-metadata
	rm -rf htmlcov junit
	rm -f coverage.xml
	rm -f .coverage

clean-test-data:
	rm -f $(STATION_DOWNLOAD_FILE)
	rm -f $(STATION_OUT_FILE)
	rm -rf .pytest_cache

clean-tox:
	rm -rf .tox

clean-all: clean clean-test-data clean-tox
