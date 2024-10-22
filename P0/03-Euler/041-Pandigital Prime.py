from itertools import permutations
from tqdm import tqdm

def find_prime(number):
    numbers = set(range(number, 1, -1))
    prime = []
    while numbers:
        x = numbers.pop()
        prime.append(x)
        multiplications_numbers = set(range(2*x, number + 1, x))
        numbers -= multiplications_numbers
    return prime

def check(x, primes):
    for prime in primes:
        if x%prime == 0:
            return False
    return True

max_number = 1_000_000_000
prime = round(max_number**0.5)
primes = find_prime(prime)

digits = ["1", "2", "3", "4", "5", "6", "7"]
possibale = list(permutations(digits, 7))
# print(possibale[0])
string_pos = [int("".join(pos)) for pos in possibale]
sorted_pos = sorted(string_pos, reverse=True)
for i in tqdm(range(len(sorted_pos))):
    # print(i)
    if check(sorted_pos[i], primes):
        print(sorted_pos[i])
        print("Hora")
        break