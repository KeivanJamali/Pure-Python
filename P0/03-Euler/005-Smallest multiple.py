def prim_dividers_factors(x: int) -> dict:
    i = 2
    xp = x
    prime_factors = dict()
    while xp != 1:
        k = 0
        while divmod(xp, i)[1] == 0:
            k += 1
            xp = xp // i
        if k != 0:
            prime_factors[i] = k
        i += 1
    return prime_factors

print(prim_dividers_factors(100))