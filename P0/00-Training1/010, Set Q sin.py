# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:35:17 2021

@author: KPS
"""

import math
Rad = [0 , math.pi/6 , math.pi/4, math.pi/3, math.pi/2]
N = ['0', 'pi/6', 'pi/4', 'pi/3', 'pi/2']
for i in range(5):
    print('sin ', N[i],'is ',math.sin(Rad[i]))
    