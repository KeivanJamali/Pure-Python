def find_prime(number):
    numbers = set(range(number, 1, -1))
    prime = []
    while numbers:
        x = numbers.pop()
        prime.append(x)
        multiplications_numbers = set(range(2*x, number + 1, x))
        numbers -= multiplications_numbers
    return prime

def rotation(prime):
    prime_str = str(prime)
    result = []
    for _ in range(len(prime_str)):
        prime_str = prime_str[-1] + prime_str[:-1]
        result.append(int(prime_str))
    return result
rotation(120)

def check(test_case, prime_list):
    for prime in test_case:
        if not prime in prime_list:
            return False
    return True

counter = 0
prime_list = find_prime(1_000_000)
for prime in prime_list:
    if check(rotation(prime), prime_list):
        counter += 1

print(counter)