"""gcd"""


def gcd(a, b):
    i = 2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            result = i
        i += 1
    return result

def gcd2(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd2(34423452352345523452342300, 24354243243243243282340))
