"""find prime numbers"""


def prime_provid(max: int) -> list:
    numbers = set(range(max, 1, -1))
    primes = []
    while numbers:
        x = numbers.pop()
        primes.append(x)
        numbers -= set(range(2 * x, max + 1, x))
    return primes


print(prime_provid(20_000_000))
