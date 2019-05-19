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