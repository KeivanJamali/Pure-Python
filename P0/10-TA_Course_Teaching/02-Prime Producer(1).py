"""find prime numbers"""


def find_prime(max: int) -> list:
    primes = []
    for i in range(2, max + 1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                primes.append(i)
    return primes


print(find_prime(200000))
