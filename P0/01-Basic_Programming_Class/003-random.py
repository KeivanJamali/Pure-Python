from random import Random
"""if empty it relates to time so it looks random always"""
List_algoritm = [Random(5), Random(1), Random(0), Random(), Random(5)]
for i in List_algoritm:
    print()
    for j in range(10):
        print(i.randint(1,10), end=" ")