""" Tests the sample data and verifies the data """

# pylint: disable=redefined-outer-name
import os
from typing import List
import pytest
from parse_bom_stations import parse_station_list, WeatherStationTuple

SAMPLE_DATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data', 'test-samples.txt')


@pytest.fixture
def station_data() -> List[WeatherStationTuple]:
    """Provides the station listing data"""
    return parse_station_list(SAMPLE_DATA)

def test_record_count(station_data: List[WeatherStationTuple]):
    """ Just used to check we load the correct number of records """
    assert len(station_data) == 6


def test_300055_site(station_data: List[WeatherStationTuple]):
    """Tests the 300055 site data"""
    station = station_data[0]
    assert station.site == '300055'
    assert station.district == '300'
    assert station.name == 'DAVIS (WHOOP WHOOP)'
    assert station.start_year == '2007'
    assert station.end_year is None
    assert float(station.latitude) == -68.4723
    assert float(station.longitude) == 78.8735
    assert station.state == 'ANT'
    assert float(station.height_m) == 593.0
    assert float(station.bar_ht) == 594.4
    assert station.wmo_id == '89570'
