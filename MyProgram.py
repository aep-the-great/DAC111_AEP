# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:50:38 2021
@author: pflug
"""

import os

os.environ["PROJ_LIB"] = "C:\\Utilities\\Python\\Anaconda\\Library\\share"; #fixr

import sqlite3 as sl
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

FLIGHTS_DB = "C:/src/DAC_111/flights.db"

def main():
    connection = sl.connect(FLIGHTS_DB)
    cursor = connection.cursor()
    
    coords = cursor.execute(
"""
select cast(longitude as float),
cast(latitude as float)
from airports;
"""
    ).fetchall()
    
    cursor.close()
    connection.close()
    
    myMap = Basemap(
        projection='merc',
        llcrnrlat=-80,
        urcrnrlat=80,
        llcrnrlon=-180,
        urcrnrlon=180,
        lat_ts=20,
        resolution='c')
    
    myMap.drawcoastlines()
    myMap.drawmapboundary()
    
    x, y = myMap([l[0] for l in coords],
                 [l[1] for l in coords])
    
    myMap.scatter(x, y, 1, marker='o',color='red')

    
    
main()
