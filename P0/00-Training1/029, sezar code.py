# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:55:33 2021

@author: KPS
"""

Eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
       'Q','R','S','T','U','V','W','X','Y','Z']
eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
       'q','r','s','t','u','v','w','x','y','z']
ans = ''
X = int(input('???'))
def main(Eng, eng):
    global ans
    global X
    a = int(input('code(1)? or decoding(2)? '))
    if a == 1:
        simp = list(input('write you statement: '))
        simp = coding(simp, Eng, eng, X)
        for i in simp:
            ans += i
        print("your code with key ", X, "is ready!: ", ans)
    elif a == 2:
        simp = list(input('write you code: '))
        X = int(input('???'))
        simp = decoding(simp, Eng, eng, X)
        for i in simp:
            ans += i
        print("we decoded it!: ", ans)
        

def coding(simp, Eng, eng, X):
    for i in range(0,len(simp)):
        for j in range(0, len(Eng)):
            if simp[i] == Eng[j]:
                simp[i] == Eng[(j + X)%26]
        for k in range(0, len(eng)):
            if simp[i] == eng[k]:
                simp[i] == eng[(k + X)%26]
    return simp
                
                
def decoding(simp, Eng, eng, X):
    for i in range(0,len(simp)):
        for j in range(0, len(Eng)):
            if simp[i] == Eng[j]:
                simp[i] == Eng[j - X]
        for k in range(0, len(eng)):
            if simp[i] == eng[k]:
                simp[i] == eng[k - X]
    return simp
                
main(Eng, eng)