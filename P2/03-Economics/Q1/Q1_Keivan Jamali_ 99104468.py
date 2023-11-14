from math import exp


def pe_p_a(i: float, n: int, a: float = None) -> float:
    """produce p from a"""
    if a:
        return a * (((1 + i) ** n - 1) / ((1 + i) ** n * i))
    else:
        return ((1 + i) ** n - 1) / ((1 + i) ** n * i)


def pe_p_f(i: float, n: int, f: float = None) -> float:
    """produce p from f"""
    if f:
        return f * (1 / (1 + i) ** n)
    else:
        return 1 / (1 + i) ** n


def pe_a_g(i: float, n: int, g: float = None) -> float:
    """produce a from g"""
    if g:
        return g * ((1 / i) - (n / (((1 + i) ** n) - 1)))
    else:
        return (1 / i) - (n / (((1 + i) ** n) - 1))


def pe_p_a1(i: float, j: float, n: int, a1: float = None) -> float:
    """produce p from a1"""
    if a1:
        if i == j:
            return a1 * ((n * a1) / (1 + i))
        else:
            return a1 * ((1 - ((1 + j) ** n) * ((1 + i) ** (-n))) / (i - j))
    else:
        if i == j:
            return (n * a1) / (1 + i)
        else:
            return (1 - ((1 + j) ** n) * ((1 + i) ** (-n))) / (i - j)


def ce_ie(r: float) -> float:
    """produce effective interest rate"""
    return exp(r) - 1


def pe_ie(r: float, m: int) -> float:
    """produce effective interest rate"""
    return (1 + r / m) ** m - 1


def ce_p_abar(r: float, n: int, abar: float = None) -> float:
    if abar:
        return abar * ((exp(r * n) - 1) / (r * exp(r * n)))
    else:
        return (exp(r * n) - 1) / (r * exp(r * n))


# S1
i = 0.15
NPW = -100 - 100 * pe_p_a(i, 3) + 200 * pe_p_a(i, 3) * pe_p_f(i, 3) + 300 * pe_p_a(i, 4) * pe_p_f(i, 6)
print(f"Question 1: NPW = {NPW}")

# S2
i = 0.1
NPW_t2 = -100 + 100 * pe_p_a(i, 2) + 200 * pe_p_a(i, 2) * pe_p_f(i, 2) + 300 * pe_p_a(i, 2) * pe_p_f(i, 4)

y = 1
NPW_t1 = y + (2 * y + y * pe_a_g(i, 6)) * pe_p_a(i, 6)
pe_a_g(i, 6), pe_p_a(i, 6)
Y = NPW_t2 / NPW_t1

x = 1
NPW_t3_plus_200 = (6 * x - x * pe_a_g(i, 6)) * pe_p_a(i, 6)
X = (NPW_t2 + 200) / NPW_t3_plus_200
print(f"Question 2: X is equal to {X} and Y is equal to {Y}")

# S3
i = 0.10
j = 0.15
# a
a1 = (900 + 300 * (pe_a_g(i, 5))) * pe_p_a(i, 5)
# b
NPW_without_A3 = -1000 - 1000 * pe_p_f(i, 1) + a1 * pe_p_f(i, 8)
NPW_A3 = pe_p_a1(i, j, 5) * pe_p_f(i, 2)
A3 = -NPW_without_A3 / NPW_A3
A4 = A3 * 1.15
# c
ie = ce_ie(i)
a1_3 = (900 + 300 * (pe_a_g(ie, 5))) * pe_p_a(ie, 5)
NPW_without_A3_3 = -1000 - 1000 * pe_p_f(ie, 1) + a1_3 * pe_p_f(ie, 8)
NPW_A3_3 = pe_p_a1(ie, j, 5) * pe_p_f(ie, 2)
A3_3 = -NPW_without_A3_3 / NPW_A3_3
A4_3 = A3_3 * 1.15
print(f"Question 3: part1: {a1} | part2: A3={A3}, A4={A4} | part3: A3={A3_3}, A4={A4_3}")

# S4
i = 0.1
# a
NPW_1 = -600 + 200 * pe_p_a(i, 5)
# b
ie = pe_ie(i, 12)
NPW_2 = -600 + 200 * pe_p_a(ie, 5)
# c
ie = ce_ie(i)
NPW_3 = -600 + 200 * pe_p_a(ie, 5)
# d
NPW_4 = -600 + 200 * ce_p_abar(i, 5)
print(f"Question 4: part1: NPW={NPW_1} | part2: NPW={NPW_2} | part3: NPW={NPW_3} | part4: NPW={NPW_4}")
