# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:11:08 2021

@author: KPS
"""

res = list(input())
ans = ''
for i in range(0, len(res), 2):
    ans += res[i]

print(ans)