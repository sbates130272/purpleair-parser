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
import argparse
from datetime import datetime

def webget(addr):

    response = requests.get(addr)
    if response.status_code != 200:
        print "Issue accessing server, %d" % response.status_code
        return None

    return response.json()

def fileget(file):

    print "Hello"

    with open(file) as json_file:
        data = json.load(json_file)
    
    return data

def savedata(data, file):

    with open(file, 'w') as outfile:
        json.dump(data, outfile)

def get_entry(jdata, idx):

    if "A_H" in jdata['results'][idx]:
        return (0, 0, 0, 0, 0, 0, 0)
    
    try:
        dA = json.loads(jdata['results'][idx]["Stats"])
        if int(jdata['results'][idx]["ID"]) % 2:
            return (0, 0, 0, 0, 0, 0, 0)
        if int(jdata['results'][idx]["ID"])+1 != int(jdata['results'][idx+1]["ID"]):
            return (0, 0, 0, 0, 0, 0, 0)
        dB = json.loads(jdata['results'][idx+1]["Stats"])
        if (float(dA['v1'])/float(dB['v1'])>0.25) and (float(dA['v1'])/float(dB['v1'])<4):
            return (jdata['results'][idx]["LastSeen"],
                    jdata['results'][idx]["ID"],
                    jdata['results'][idx]["Lat"],
                    jdata['results'][idx]["Lon"],
                    dA['v1'],
                    jdata['results'][idx+1]["ID"],
                    dB['v1'])
        else:
            return (0, 0, 0, 0, 0, 0, 0)
    except:
        return (0, 0, 0, 0, 0, 0, 0)

def parse_purple(jdata):

    unsorted_data = []
    for i in xrange(1, len(jdata['results'])):
        val = get_entry(jdata, i)
        unsorted_data.append(val)

    sorted_data = sorted(unsorted_data, key= lambda tup: tup[4])

    for i in xrange(-20, 0):
        print sorted_data[i]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Fetch and process purpleair.com data.')
    parser.add_argument('--webget', action='store_true',
                        help='get JSON data from web.')
    parser.add_argument('--save', action='store_true',
                        help='save JSON data to file.')

    args = parser.parse_args()

    if args.webget:
        jdata = webget('https://www.purpleair.com/json')
    else:
        jdata = fileget('json.in.txt')

    if args.save:
        savedata(jdata, 'json.out.txt')
    
    parse_purple(jdata)
