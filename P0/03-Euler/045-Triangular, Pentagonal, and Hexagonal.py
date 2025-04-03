import math

def hexagonal(n):
    return n * (2 * n - 1)

def is_pentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n.is_integer()

def is_triangular(x):
    n = (-1 + math.sqrt(8 * x + 1)) / 2
    return n.is_integer()

n = 144

while True:
    H_n = hexagonal(n)
    if is_pentagonal(H_n) and is_triangular(H_n):
        print(f"Found: {H_n} and n = {n}")
        break
    n += 1 
