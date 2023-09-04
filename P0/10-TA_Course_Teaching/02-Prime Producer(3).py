"""find prime numbers"""


def find_prime(max: int) -> list:
    primes = [2, 3]
    for i in range(5, max + 1, 2):
        temp = 0
        for j in primes:
            if i % j == 0:
                break
            temp += 1
            if temp == len(primes):
                primes.append(i)
    return primes


print(find_prime(20000000))
