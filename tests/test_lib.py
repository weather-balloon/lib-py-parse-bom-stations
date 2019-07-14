""" Tests the data load and verifies the data """

# pylint: disable=redefined-outer-name
import os
import pytest
from parse_bom_stations import parse_station_list


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data',
)

STATIONDATA = pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'bomstations.txt')
)


@STATIONDATA
def test_load(datafiles):
    """ Just used to check the data loads some records """
    for station_data in datafiles.listdir():
        results = parse_station_list(station_data)
        assert results.shape[0] > 0


@STATIONDATA
def test_fields_site(datafiles):
    """ All records MUST have a site """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['site']:
            assert entry


@STATIONDATA
def test_fields_start_year(datafiles):
    """ All records MUST have a start_year """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['start_year']:
            assert len(entry) == 4
            assert 1700 <= int(entry) <= 3000


@STATIONDATA
def test_fields_wmo_id(datafiles):
    """ All records MAY have a wmo_id of 5 characters """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['wmo_id']:
            assert (entry is None or len(entry) == 5)


@STATIONDATA
def test_fields_end_year(datafiles):
    """ All records MAY have an end year """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['end_year']:
            assert (entry is None or
                    (len(entry) == 4 and
                     1700 <= int(entry) <= 3000))


@STATIONDATA
def test_fields_latitude(datafiles):
    """ All records MUST have latitude that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['latitude']:
            assert entry is not None

            try:
                float(entry)
            except ValueError:
                pytest.fail(
                    "Failed to convert to float: {}".format(entry))


@STATIONDATA
def test_fields_longitude(datafiles):
    """ All records MUST have logitude that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['longitude']:
            assert entry is not None

            try:
                float(entry)
            except ValueError:
                pytest.fail(
                    "Failed to convert to float: {}".format(entry))


@STATIONDATA
def test_fields_state(datafiles):
    """ All records MUST have a valid state """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['state']:
            assert 2 <= len(entry) < 4
            assert entry in ['WA',
                             'NT',
                             'QLD',
                             'NSW',
                             'VIC',
                             'TAS',
                             'SA',
                             'ISL',
                             'ANT']


@STATIONDATA
def test_fields_source(datafiles):
    """ All records MAY have a a lat/long source """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['source']:

            assert (entry in [None,
                              'Unknown',
                              'GPS',
                              'SURVEY']
                    or entry.startswith('MAP')
                    or entry.startswith('DEM'))


@STATIONDATA
def test_fields_district(datafiles):
    """ All records MAY have a district """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['district']:
            assert (entry is None or 1 <= len(entry) <= 4)


@STATIONDATA
def test_fields_height_m(datafiles):
    """ All records MAY have a height_m that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['height_m']:
            if entry is not None:
                try:
                    float(entry)
                except ValueError:
                    pytest.fail(
                        "Failed to convert to float: {}".format(entry))


@STATIONDATA
def test_fields_bar_ht(datafiles):
    """ All records MAY have a bar_ht that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list['bar_ht']:
            if entry is not None:
                try:
                    float(entry)
                except ValueError:
                    pytest.fail(
                        "Failed to convert to float: {}".format(entry))
