# -*- coding: utf-8 -*-
# 001 29/01/17 MRT Added variable X for testing
"""
Created on Sat Jan 21 21:13:17 2017

@author: Robela
"""
import json
import requests
import json
import matplotlib
from byteifythis import byteifythis

class WeatherForecast(object):
    name = ""
    clouds = ""
    coord = ""
    sys = ""
    
    def __init__(self, j):
        self.__dict__ = json.loads(j)
    
if __name__ == "__main__":

    id1 = '524901'
    appID = '9a7f0ae578e3b306d59fc50002451513'
    print("Enter a city name (e.g. London,uk)")
    location = raw_input()
        
    url = 'http://api.openweathermap.org/data/2.5/weather?id={0}&APPID={1}&q={2}'.format(id1, appID, location)
    myResponse = requests.get(url, verify=True)
    print (myResponse.status_code)
    
    if(myResponse.ok):        
        p = WeatherForecast(myResponse.content)
        print(p.clouds)              
    else:
      # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
      # -001
      x = 5
      # +001