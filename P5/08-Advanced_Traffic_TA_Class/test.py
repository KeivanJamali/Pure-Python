import random

# print(round(random.random()))
a = 0
while a in [0, 14, 11, 1, 5]:
    a = round(14*random.random())
    
print(a)

network = r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/SiouxFallsNetwork.csv"
xy = r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/SiouxFallsXY.csv"