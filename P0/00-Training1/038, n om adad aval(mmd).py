# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:29:09 2021

@author: KPS
"""

def adad_aval_yab(adad):
    if adad>=2 and type(adad)==type(1):
        adadhai_aval=[2]
        yield 2
        for x in range(3,adad+1,2):
            aval_hast=True
            for aval in adadhai_aval[1::]:
                if x>=aval**2:
                    if x%aval==0:
                        aval_hast=False
                        break
                else:
                    break
            if aval_hast:
                adadhai_aval.append(x)
                yield x
    else:
        yield "ValueError"

for x in adad_aval_yab(100000):
    print(x)