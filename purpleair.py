#!/usr/bin/env python
#
# (c) Stephen Bates, Raithlin Semiconductors, 2019
#
# purpleair.py
# ------------
#
# A simple python tool to pull data from the purpleair.com database
# and parse the json based data.

import json
import requests

if __name__ == "__main__":
    response = requests.get('https://www.purpleair.com/json')

    if response.status_code != 200:
        print "Issue accessing server, %d" % response.status_code
        exit -1
    
    print response.json()
