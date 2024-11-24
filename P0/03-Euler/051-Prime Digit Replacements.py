from itertools import permutations

def prime_provid(n):
    """n = last_number"""
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        x = numbers.pop()
        primes.append(x)
        numbers -= set(range(2 * x, n + 1, x))
    return primes

primes = prime_provid(10_000_000)


book = {"1":[],"2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[]}
for prime in primes:
    book[str(len(str(prime)))].append(prime)

def check(numbers:list):
    book2 = {}
    for number in numbers:
        if not str(number) in book2.keys():
            book2[str(number)] = 0
        else:
            book2[str(number)] += 1
    for k, v in book2.items():
        if v == 6:
            return k
    return False

def main():
    for k, v in book.items():
        if k == "1":
            continue
        
        if k == "2":
            for digit in range(1, int(k)):
                tx = list(digit * "1" + (int(k)-digit) * "0")
                comb = set(permutations(tx, int(k)))
                for c in comb:
                    for a in range(len(c)):
                        if c[a] == "1":
                            result = []
                            for number in v:
                                result.append(int("".join(list(str(number)).pop(a))))
                            
                            bool_ = check(result)
                            if bool_:
                                return bool_
                            
print(main())