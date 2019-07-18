""" Parses weather stations published by the Australian Bureau of Meteorology """

from .parse_bom_stations import parse_station_list, parse_station_list_to_csv, parse_station_list_to_json
from .about import NAME, AUTHOR, AUTHOR_EMAIL, CLASSIFIERS, LICENCE

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
