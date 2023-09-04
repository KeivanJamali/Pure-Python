class A():
    a = None

class B():
    def __init__(self):
        self.b = 0

    def __str__(self):
        return repr(self.b)

A().a = B()
f = A()
f.a = B()
print(A().a)
print(f.a)