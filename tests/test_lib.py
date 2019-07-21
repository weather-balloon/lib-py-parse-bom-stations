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
        assert results


@STATIONDATA
def test_fields_site(datafiles):
    """ All records MUST have a site """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert entry.site


@STATIONDATA
def test_fields_start_year(datafiles):
    """ All records MUST have a start_year """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert len(entry.start_year) == 4
            assert 1700 <= int(entry.start_year) <= 3000


@STATIONDATA
def test_fields_wmo_id(datafiles):
    """ All records MAY have a wmo_id of 5 characters """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert (entry.wmo_id is None or len(entry.wmo_id) == 5)


@STATIONDATA
def test_fields_end_year(datafiles):
    """ All records MAY have an end year """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert (entry.end_year is None or
                    (len(entry.end_year) == 4 and
                     1700 <= int(entry.end_year) <= 3000))


@STATIONDATA
def test_fields_latitude(datafiles):
    """ All records MUST have latitude that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert entry.latitude is not None

            try:
                float(entry.latitude)
            except ValueError:
                pytest.fail(
                    "Failed to convert to float: {}".format(entry.latitude))


@STATIONDATA
def test_fields_longitude(datafiles):
    """ All records MUST have logitude that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert entry is not None

            try:
                float(entry.longitude)
            except ValueError:
                pytest.fail(
                    "Failed to convert to float: {}".format(entry.longitude))


@STATIONDATA
def test_fields_state(datafiles):
    """ All records MUST have a valid state """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert 2 <= len(entry.state) < 4
            assert entry.state in ['WA',
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
        for entry in station_list:

            assert (entry.source in [None,
                                     'Unknown',
                                     'GPS',
                                     'SURVEY']
                    or entry.source.startswith('MAP')
                    or entry.source.startswith('DEM'))


@STATIONDATA
def test_fields_district(datafiles):
    """ All records MAY have a district """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            assert (entry.district is None or 1 <= len(entry.district) <= 4)


@STATIONDATA
def test_fields_height_m(datafiles):
    """ All records MAY have a height_m that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            if entry.height_m is not None:
                try:
                    float(entry.height_m)
                except ValueError:
                    pytest.fail(
                        "Failed to convert to float: {}".format(entry.height_m))


@STATIONDATA
def test_fields_bar_ht(datafiles):
    """ All records MAY have a bar_ht that can be converted to float """
    for station_data in datafiles.listdir():
        station_list = parse_station_list(station_data)
        for entry in station_list:
            if entry.bar_ht is not None:
                try:
                    float(entry.bar_ht)
                except ValueError:
                    pytest.fail(
                        "Failed to convert to float: {}".format(entry.bar_ht))
