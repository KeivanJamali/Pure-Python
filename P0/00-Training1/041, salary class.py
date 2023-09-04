# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:33:11 2021

@author: KPS
"""

class Teacher:
    def __init__(self,Id, first_name, last_name, workhour, salary_hour):
        self.Id = Id
        self.first = first_name
        self.last = last_name
        self.hours = workhour
        self.eachsalary = salary_hour
        self.salary = 0
    
    
    def __str__(self):
        print('id = ', self.Id, 'and name is: ', self.first,' ', self.last
              ,'and this teache worked ',self.hours,' hours and his salary is '
              ,self.hours * self.eachsalary)
    
    
    
