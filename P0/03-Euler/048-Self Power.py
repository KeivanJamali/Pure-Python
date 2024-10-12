def power(a:int, bin:str, m:int):
    result = a % m
    bin = bin[1:]
    for i in list(bin):
        result = (result * result) % m
        if i == "1":
            result = (result * a) % m
    return result

def main(last_digits:int, a_list:list):
    m = 10**last_digits
    result = 0
    for a in a_list:
        binary = bin(a)[2:]
        result = (result + power(a, binary, m)) % m
    return result

# print(list(range(1, 1001)))
print(main(10, list(range(1, 1001))))

# print(power(20, bin(2)[2:], 1000000))