# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:22:32 2021

@author: KPS
"""

def Per(self):
    
    """You put a Number and then it will tell you if it's Perfected or not."""
    
    if self == 0:
        Number = int(input('Give me a nimber to check please: '))
        for a in range(1,Number):
            List = divmod(Number, a)
            remaning = List[1]
            if remaning == 0:
                self += a
        if self == Number :
            print ('\t','Perfected!')
        else:
            print('\t','Not Perfected!')
    self = 0
    Repeat = input('do you want to do it again? ')
    if Repeat == 'yes' or Repeat == 'Yes':
        print(Per(self))
    elif Repeat == 'No' or Repeat == 'no':
        return 'thank you!'
    else:
        print ('please write yes or no.')      
    
A = 0
print(Per(A))