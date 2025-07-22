import math

def parallelogram_area(b: float, h: float) -> float:
    return b * h

def cylinder_volume_area(r: float, h: float) -> tuple[float, float]:
    return math.pi * r**2 * h, math.pi * 2 * r**2 + 2 * math.pi * r * h

def sphere_volume_area(r: float) -> tuple[float, float]:
    return (4/3) * math.pi * r**3, 4 * math.pi * r**2

def polygon_area(n: int, s: float) -> float:
    return (n * s**2) / (4 * math.tan(math.pi/n))

def age_to_seconds(age: int) -> int:
    return age * 365 * 24 * 60 * 60

def magic_word(text: str) -> str:
    return text[::2]

def printint(name: str) -> None:
    print(name.upper())
    print(name.lower())
    print(name.title())
    print(f"your name has {len(name)} characters.")
    print(name[::-1])

def replace_in_sentence(text: str, inplace:str) -> str:
    return text.replace("___", inplace)

def count_letters(text: str, letter: str) -> int:
    return text.count(letter)

def sort_3_numbers_function(a, b, c) -> list:
    if a > b:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return [a, b, c]

def multiples_of_numbers(max_number: int, numbers_list: int) -> int:
    result = set()
    for i in numbers_list:
        result = result | set(range(i, max_number, i))
    return result

def fibonacci(n: int) -> list:
    result = [1, 2]
    temp1 = 1
    temp2 = 2
    for _ in range(n):
        temp1, temp2 = temp2, temp1 + temp2
        result.append(temp2)
    return result

def prime_factors(number: int) -> list:
    prime_f = []
    temp = number
    for i in range(2, number):
        while temp%i == 0:
            temp = temp // i
            prime_f.append(i)
    return prime_f

def prime_provider(n: int) -> list:
    """n = last_number"""
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        x = numbers.pop()
        primes.append(x)
        numbers -= set(range(2 * x, n + 1, x))
    return primes
