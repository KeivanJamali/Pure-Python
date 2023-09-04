# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:53:21 2021

@author: KPS
"""

foot = inch = 0
foot_m = foot_cm = inch_m = inch_cm = 0

def read():
    global foot, inch
    foot = float(input('Foot? '))
    inch = float(input('inch? '))


def calculate():
    global foot_m, foot_cm, inch_m, inch_cm
    foot_m = foot * 0.3048
    foot_cm = foot * 0.3048 * 100
    inch_m = inch/12 *0.3048
    inch_cm = inch/12 * 0.3048*100

    
def write():
    print(foot,'foot is ',foot_cm,'centimeter.')
    print(foot,'foot is ',foot_m,'meter.')
    print(inch,'inches is ',inch_cm,'centimeter.')
    print(inch,'inches is',inch_m,'meter.')
    
def main():
    read()
    calculate()
    write()
    
main()