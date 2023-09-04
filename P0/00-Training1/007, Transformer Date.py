# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:53:52 2021

@author: KPS
"""

import datetime as dt
date = [int(input("write you birth year: " )),
        int(input("write you birth month: " )),
        int(input("write you birth day: " ))]
now = dt.datetime.today()
dif = [now.year - date[0], now.month - date[1], now.day - date[2]]
if dif[2] < 0 :
    dif[1] = dif[1] - 1
    dif[2] += 30
if dif[1] < 0 :
    dif[0] = dif[0] - 1
    dif[1] = dif[1] + 12
print(dif)


    
