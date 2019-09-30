#!/usr/bin/env python3

# To use locally, make sure you run:
#   sudo pip3 install -e .

import sys
import urllib.request
from io import StringIO
from parse_bom_stations import parse_station_list_to_json

if (len(sys.argv) > 1):
    station_data = sys.argv[1]
else:
    data_url = 'ftp://ftp.bom.gov.au/anon2/home/ncc/metadata/sitelists/stations.txt'

    with urllib.request.urlopen(data_url) as response:
        bytes_data = response.read()

    station_data = StringIO(str(bytes_data, 'ascii'), newline="\r\n")

print(parse_station_list_to_json(station_data))
