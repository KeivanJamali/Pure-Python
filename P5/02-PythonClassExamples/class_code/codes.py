import math
from sympy import prime

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
    if n < 2:
        return []
    numbers = set(range(2, n + 1))
    primes = []
    for x in range(2, n + 1):
        if x in numbers:
            primes.append(x)
            numbers -= set(range(2 * x, n + 1, x))
    return primes

def atkin_sieve(limit: int) -> list:
    if limit < 2:
        return []

    sieve = [False] * (limit + 1)
    sqrt_limit = int(math.sqrt(limit)) + 1

    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and n % 12 in (1, 5):
                sieve[n] ^= True

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            if x > y:
                n = 3 * x ** 2 - y ** 2
                if n <= limit and n % 12 == 11:
                    sieve[n] ^= True

    for i in range(5, sqrt_limit):
        if sieve[i]:
            for j in range(i * i, limit + 1, i * i):
                sieve[j] = False

    # 2 and 3 are known primes
    primes = [2, 3] + [i for i in range(5, limit + 1) if sieve[i]]
    return primes

def provide_pimes2(n: int) -> list:
    return prime(n)

def sum_square_difference(start_n: int, end_n: int) -> int:
    numbers = list(range(start_n, end_n+1))
    sums = 0
    ssum = 0
    for n in numbers:
        sums += n**2
        ssum += n
    ssum = ssum**2
    return abs(ssum - sums)

def largest_product_in_a_series(n: int) -> int:
    input_number = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
    best_answer = 0
    for i in range(len(input_number)-n):
        s = 1
        for j in range(n):
            s *= int(input_number[i+j])
        if s > best_answer:
            best_answer = s
    return best_answer
