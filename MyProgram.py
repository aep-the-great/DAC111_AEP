# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:50:38 2021
@author: pflug
"""

import sqlite3 as sl

FLIGHTS_DB = "C:/src/DAC_111/flights.db"

def main():
    connection = sl.connect(FLIGHTS_DB)
    cursor = connection.cursor()
    
    query = "select * from airlines limit 5;"
    cursor.execute(query)
    
    results = cursor.fetchall()
    print(results)
    
    cursor.close()
    connection.close()
    
    
main()
