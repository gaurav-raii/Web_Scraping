# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:10:40 2019

@author: gaura
"""

from bs4 import BeautifulSoup
soup= BeautifulSoup(open("virgin_and_logan_airport.html"))
option_values=[]
carrier_list= soup.find(id="CarrierList")
for option in carrier_list.find_all('option'):
    option_values.append(option['value'])
    
Carriers =option_values     # list of carriers

option_values=[]
airport_list= soup.find(id="AirportList")
for option in airport_list.find_all('option'):
    option_values.append(option['value'])
Airports= option_values


import requests

s= requests.session()
r= s.get("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2")

soup= BeautifulSoup(r.text)
vs = soup.find(id="__VIEWSTATE")
viewstate= vs["value"]
ev = soup.find(id="__EVENTVALIDATION")
eventvalidation= ev["value"]

r=s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
data={'AirportList': "BOS",