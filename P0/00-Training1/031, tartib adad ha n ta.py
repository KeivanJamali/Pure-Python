# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:13:28 2021

@author: KPS
"""
L = []
n = int(input())
for i in range(0, n):
    L.append(int(input('Enter '+str(i+1)+' number: ')))
L2 = L.copy()

for p in range(0, n):
    for j in range(0, p):
        for k in range(p, n):
            if L[j] > L[k]:
                temp = L[j]
                L[j] = L[k]
                L[k] = temp
for i in range(0, n):
    if L[0] == L2[i]:
        print('the lowest is ', i + 1, 'ed')
    if L[-1] == L2[i]:
        print('the highest is ', i + 1, 'ed')
print('min is ', L[0], 'and max is ', L[-1])


# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# b1 = a1
# b2 = a2
# b3 = a3
# if a1 > a2:
#     temp = a1
#     a1 = a2
#     a2 = temp
# if a1 > a3:
#     temp = a1
#     a1 = a3
#     a3 = temp
# if a2 > a3:
#     temp = a2
#     a2 = a3
#     a3 = temp
# if a1 == b1:
#     print('1 the lowest!')
# elif a1 == b2:
#     print('2 the lowest!')
# elif a1 == b3:
#     print('3 the lowest!')
# if a3 == b1:
#     print('1 the highest!')
# elif a3 == b2:
#     print('2 the highest!')
# elif a3 == b3:
#     print('3 the highest!')
    