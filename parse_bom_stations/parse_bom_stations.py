""" Parses weather stations published by the Australian Bureau of Meteorology """

import sys
from pathlib import Path
from typing import NamedTuple, List
import pandas as pd


class WeatherStationTuple(NamedTuple):
    """ Data class for a weather station """
    site: str
    district: str
    name: str
    start_year: int
    end_year: int
    latitude: float
    longitude: float
    source: str
    state: str
    height_m: float
    bar_ht: float
    wmo_id: int


COLSPEC = '------- ----- ---------------------------------------- ' \
    '------- ------- -------- --------- -------------- --- ---------- -------- ------'


def _get_colspec(station_cols: str = COLSPEC):

    station_col_specification = []

    col_start = 0
    idx = 0

    for idx, char in enumerate(station_cols):
        if char == ' ':
            station_col_specification.append((col_start, idx))
            col_start = idx + 1

    station_col_specification.append((col_start, idx + 1))

    return station_col_specification


def _parse_station_list(filepath_or_buffer) -> pd.DataFrame:
    """Parses the fixed-width station listing

    :param filepath_or_buffer: stations file (stations.txt)
    :type filepath_or_buffer: str, path object, or file-like object
    :return: A list of weather stations
    :rtype: List[WeatherStationTuple]
    """

    station_df = pd.read_fwf(filepath_or_buffer,
                             header=2,
                             na_values=['..', '.....'],
                             skip_blank_lines=True,
                             skipfooter=6,
                             colspecs=_get_colspec())

    station_df.drop(index=0, inplace=True)

    station_df.columns = ['site', 'district', 'name', 'start_year', 'end_year',
                          'latitude', 'longitude', 'source', 'state', 'height_m', 'bar_ht', 'wmo_id']

    station_df.where((pd.notnull(station_df)), None, inplace=True)

    return station_df


def parse_station_list_to_json(filepath_or_buffer) -> str:
    """ Return JSON-formatted data """
    return _parse_station_list(filepath_or_buffer).to_json(orient="records")


def parse_station_list_to_csv(filepath_or_buffer) -> str:
    """ Return CSV-formatted data """
    return _parse_station_list(filepath_or_buffer).to_csv()


def parse_station_list(filepath_or_buffer) -> List[WeatherStationTuple]:
    """ Return Tuple list """
    return list(_parse_station_list(filepath_or_buffer)
                .itertuples(index=False,
                            name='WeatherStationTuple'))


def cli(args):
    """ A very basic command line """
    if len(args) >= 2 and args[1] in ['-h', '--help']:
        print(f'Usage: {args[0]} INPUT_FILE [csv]')
        exit(0)

    if len(args) < 2:
        print('Expected parameter: path to input file')
        exit(-1)

    input_file = Path(args[1])

    if not input_file.exists():
        print(f'The requested input file does not exist: {input}')

    if len(args) > 2 and args[2] == 'csv':
        result = parse_station_list_to_csv(input_file)
    else:
        result = parse_station_list_to_json(input_file)

    print(result)


if __name__ == '__main__':
    cli(sys.argv)
