def f_p(i, n, p=None):
    if p:
        return p * ((1 + i) ** n)
    else:
        return (1 + i) ** n


def p_f(i, n, f=None):
    if f:
        return f * (1 / (1 + i) ** n)
    else:
        return 1 / (1 + i) ** n


def p_a(i, n, a=None):
    if a:
        return a * (((1 + i) ** n - 1) / ((1 + i) ** n * i))
    else:
        return ((1 + i) ** n - 1) / ((1 + i) ** n * i)


def a_p(i, n, p=None):
    if p:
        return p * (((1 + i) ** n * i) / ((1 + i) ** n - 1))
    else:
        return ((1 + i) ** n * i) / ((1 + i) ** n - 1)


def f_a(i, n, a=None):
    if a:
        return a * (i / ((1 + i) ** n - 1))
    else:
        return i / ((1 + i) ** n - 1)


def a_f(i, n, f=None):
    if f:
        return f * (((1 + i) ** n - 1) / i)
    else:
        return ((1 + i) ** n - 1) / i


def p_g(i, n, g=None):
    if g:
        return g * ((1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n)))
    else:
        return (1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n))


def a_g(i, n, g=None):
    if g:
        return g * ((1 / i) - (n / (((1 + i) ** n) - 1)))
    else:
        return (1 / i) - (n / (((1 + i) ** n) - 1))


def p_a1(i, j, n, a1=None):
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


def f_a1(i, j, n, a1=None):
    if a1:
        if i == j:
            return a1 * (n * (1 + j) ** (n - 1))
        else:
            return a1 * ((((1 + i) ** n) - ((1 + j) ** n)) / (i - j))
    else:
        if i == j:
            return n * (1 + j) ** (n - 1)
        else:
            return (((1 + i) ** n) - ((1 + j) ** n)) / (i - j)


def rg(parameters: list):
    answer = 1
    for i in parameters:
        answer *= (i + 1)
    return answer ** (1 / len(parameters)) - 1