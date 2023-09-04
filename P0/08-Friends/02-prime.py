def prime(n: int, nts: int) -> int:
    """give you nts(step) prime number which is below n(a number)"""
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        x = numbers.pop()
        primes.append(x)
        numbers -= set(range(2 * x, n + 1, x))
    # return [primes[-1], primes[-2], len(primes)]
    primes = sorted(primes)
    return primes[nts]

print(prime(1000000, 10001))


