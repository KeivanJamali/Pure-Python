
"""first inheritsnce"""

# class A:
#     def show(self):
#         print('Show')
#
# class B:
#     def say(self):
#         print('say')
#
# class C(A, B):
#     def c(self):
#         A.show(self)
#         B.say(self)
#
# c = C()
# c.c()
# c.say()



"""problem not solved"""

# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def show(self):
#         return f'{self.name} --> {self.speed}'
#
# class Car:
#     def name(self):
#         return f'car: {self.name}'
#
# class Motor:
#     def name(self):
#         return f'motor: {self.name}'
#
# class Toyota(Car, Vehicle):
#     pass
#
# class Retro(Motor, Vehicle):
#     pass
#
# me = Toyota('cor', 200)
# notme = Retro('idk', 60)
# print(me.show(), me.name())
# print(notme.name())



"""jfjfjfjf"""

# class A:
#     a_call = 0
#
#     def call(self):
#         print('AAA')
#         A.a_call += 1
#
#
# class B(A):
#     b_call = 0
#
#     def call(self):
#         print('BBB')
#         B.b_call += 1
#         super().call()
#
#
# class C(A):
#     c_call = 0
#
#     def call(self):
#         print('CCC')
#         C.c_call += 1
#         super().call()
#
#
# class D(C, B):
#     d_call = 0
#
#     def call(self):
#         print("DDD")
#         D.d_call += 1
#         super().call()
#
#
# ans = D()
# ans.call()


"""**kwargs"""
# class A:
#     def call(self, a='', **kwargs):
#         print('a')
#
# class B(A):
#     def call(self, b='', a='', **kwargs):
#         print(a, b)
#         kwargs['a'] = a
#         kwargs['b'] = b
#         super().call(**kwargs)
#
#
# class C(A):
#     def call(self, c='', a='', b='', **kwargs):
#         print(a, b, c)
#         kwargs['a'] = a
#         kwargs['b'] = b
#         super().call(**kwargs)
#
#
# class D(B, C):
#     def call(self, d='', **kwargs):
#         print(d)
#         super().call(**kwargs)
#
# ans = D()
# ans.call(a='10', b='20', c='30', d='40')


