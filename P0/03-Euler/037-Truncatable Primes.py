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
    x_list = list(str(x))
    x_str = str(x)
    for char_i in range(1, len(x_list)):
        if int(x_list[char_i])%2==0 or int(x_list[char_i])%5==0 or x_list[char_i]=="0":
            return False
    
    # right to left
    for i in range(1, len(x_list)):
        if not int(x_str[:-i]) in primes:
            return False
    
    # left to right
    for i in range(1, len(x_list)):
        # print(x_str[i:])
        if not int(x_str[i:]) in primes:
            return False
    return True

prime_list = find_prime(1_000_000)
result = []
for prime_i in tqdm(range(4, len(prime_list))):
    if check(prime_list[prime_i], prime_list):
        result.append(prime_list[prime_i])
print(result)