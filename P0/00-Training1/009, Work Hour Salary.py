# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:02:54 2021

@author: KPS
"""

n = int(input('how many people you want to add? '))
i = 1
while i <= n:
    Id = int(input('Your Number? ')) #Work_number
    Wh = int(input('hour? ')) #Work_hour
    Sh = int(input('each hour Salary? ')) #Salary_hour
    if Wh <= 40:
        S = Wh*Sh
    else:
        S = 40*Sh + (Wh-40)*Sh*3/2
    print('id: ',Id,'Salary: ', S)
    i += 1
