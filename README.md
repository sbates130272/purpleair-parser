Introduction
------------

This is a simple python based parser for the [PurpleAir air monitoring
website](https://www.purpleair.com/). And an associated data file of
data collected from that site. The parser does two things:

 1. Obtains and dumps the 25 outside locations with the highest
 readings at the time of collection. Note we do filter out any
 readings where left and right sensors vary by too much.
 2. Obtains and dumps the reading for my own sensor in Canmore,
 Alberta (sensor ).

Usage
-----
You can get the data from the PurpleAir website using the following
command.

> ./purpleair.py --webget

There are a few other options to the Python script. Type

> ./purpleair.py -h

for those.
