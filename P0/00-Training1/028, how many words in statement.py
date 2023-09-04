# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:28:37 2021

@author: KPS
"""

def tekrar(word, statement, dic):
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
    
    
    
def main():
    statement = list(input('write an statement: '))
    word = ''
    List =[]
    dic = dict()
    for i in range(len(statement)):
        if statement[i] == ' ':
            List.append(word)
            word = ''
        else:
            word += statement[i]
    List.append(word)
    for i in range(0, len(List)):
        tekrar(List[i], statement, dic)
    print(dic)
    
main()