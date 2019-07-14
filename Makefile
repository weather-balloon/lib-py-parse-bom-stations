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
	/usr/bin/env python3 -m pip install pipenv --upgrade
	pipenv install --dev

check:
	pipenv check

lint:
	pipenv run pylint $(PACKAGE) tests bin

fetch-data:
	bin/fetch_bom_stations $(STATION_DOWNLOAD_FILE) $(STATION_OUT_FILE)

test: fetch-data
	pipenv run tox

package: clean lint check test
	pipenv run python setup.py sdist bdist_wheel

publish: package
	pipenv run twine upload dist/*

clean:
	pipenv clean
	rm -rf build dist .egg .eggs *.egg-info pip-wheel-metadata
	rm -f $(STATION_DOWNLOAD_FILE)
	rm -f $(STATION_OUT_FILE)

#clean-tox:
#	rm -rf .tox
