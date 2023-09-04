from math import pi


class Circle:
    def __init__(self, r):
        self.r = r
        self.area = pi * r * r
        self.perime = 2 * pi * r

    def __str__(self):
        s = f"R is: {self.r:.2f}\t\tand area is: {self.area:.2f}\t\t\tand perime is: {self.perime:.3f}"
        return s

    def __del__(self):
        print("object deleted")


r = int(input("Enter the R: "))
obj = Circle(r)
print(obj)
del obj
