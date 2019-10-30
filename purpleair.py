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

def parse_purple(jdata):

#    print json.dumps(jdata, indent=4, sort_keys=True)

    print jdata['results'][0]
    print jdata['results'][0]["Lat"]
    print jdata['results'][0]["Lon"]
    d = json.loads(jdata['results'][0]["Stats"])
    print d['v']

    # {
    # "baseVersion": "6", 
    # "mapVersion": "0.95", 
    # "mapVersionString": "", 
    # "results": [
    #     {
    #         "AGE": 0, 
    #         "DEVICE_LOCATIONTYPE": "outside", 
    #         "Hidden": "false", 
    #         "ID": 16791, 
    #         "Label": " DW0435", 
    #         "LastSeen": 1572398501, 
    #         "Lat": 18.082454, 
    #         "Lon": -67.039027, 
    #         "PM2_5Value": "4.11", 
    #         "Stats": "{\"v\":4.11,\"v1\":3.41,\"v2\":3.36,\"v3\":3.39,\"v4\":3.22,\"v5\":2.64,\"v6\":3.24,\"pm\":4.11,\"lastModified\":1572398501693,\"timeSinceModified\":119561}", 
    #         "THINGSPEAK_PRIMARY_ID": "589048", 
    #         "THINGSPEAK_PRIMARY_ID_READ_KEY": "61GKVZGTCZSBUGB5", 
    #         "THINGSPEAK_SECONDARY_ID": "589049", 
    #         "THINGSPEAK_SECONDARY_ID_READ_KEY": "5HBLH5R8GPLM6J88", 
    #         "Type": "PMS5003+PMS5003+BME280", 
    #         "humidity": "65", 
    #         "isOwner": 0, 
    #         "pressure": "1007.79", 
    #         "temp_f": "87"
    #     }, 



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
