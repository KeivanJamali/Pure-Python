from math import exp


class Eco:
    def __init__(self):
        self.decimal_digits = 4

    def print_factor(self, factor: float, name: str) -> None:
        print(f"__{name} = {factor:.{self.decimal_digits}f}__")


class Primary_Eco(Eco):
    def __init__(self, decimal_digits: int = 4):
        super().__init__()
        self.decimal_digits = decimal_digits

    def f_p(self, i: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce f from p"""
        factor = (1 + i) ** n
        if print_:
            self.print_factor(factor=factor, name=f"(F/P, {i:.{self.decimal_digits}f}, {n})")
        if p:
            return p * factor
        else:
            return factor

    def p_f(self, i: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce p from f"""
        factor = 1 / (1 + i) ** n
        if print_:
            self.print_factor(factor=factor, name=f"(P/F, {i:.{self.decimal_digits}f}, {n})")
        if f:
            return f * factor
        else:
            return factor

    def p_a(self, i: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce p from a"""
        factor = ((1 + i) ** n - 1) / ((1 + i) ** n * i)
        if print_:
            self.print_factor(factor=factor, name=f"(P/A, {i:.{self.decimal_digits}f}, {n})")
        if a:
            return a * factor
        else:
            return factor

    def a_p(self, i: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce a from p"""
        factor = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/P, {i:.{self.decimal_digits}f}, {n})")
        if p:
            return p * factor
        else:
            return factor

    def f_a(self, i: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce f from a"""
        factor = ((1 + i) ** n - 1) / i
        if print_:
            self.print_factor(factor=factor, name=f"(F/A, {i:.{self.decimal_digits}f}, {n})")
        if a:
            return a * factor
        else:
            return factor

    def a_f(self, i: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce a from f"""
        factor = i / ((1 + i) ** n - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/F, {i:.{self.decimal_digits}f}, {n})")
        if f:
            return f * factor
        else:
            return factor

    def p_g(self, i: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce p from g"""
        factor = (1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/G, {i:.{self.decimal_digits}f}, {n})")
        if g:
            return g * factor
        else:
            return factor

    def a_g(self, i: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce a from g"""
        factor = (1 / i) - (n / (((1 + i) ** n) - 1))
        if print_:
            self.print_factor(factor=factor, name=f"(A/G, {i:.{self.decimal_digits}f}, {n})")
        if g:
            return g * factor
        else:
            return factor

    def p_a1(self, i: float, j: float, n: int, a1: float = None, print_: bool = True) -> float:
        """produce p from a1"""
        factor1 = (n * a1) / (1 + i)
        factor2 = (1 - ((1 + j) ** n) * ((1 + i) ** (-n))) / (i - j)
        if a1:
            if i == j:
                if print_:
                    self.print_factor(factor=factor1,
                                      name=f"(P/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return a1 * factor1
            else:
                if print_:
                    self.print_factor(factor=factor2,
                                      name=f"(P/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return a1 * factor2
        else:
            if i == j:
                if print_:
                    self.print_factor(factor=factor1,
                                      name=f"(P/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return factor1
            else:
                if print_:
                    self.print_factor(factor=factor2,
                                      name=f"(P/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return factor2

    def f_a1(self, i: float, j: float, n: int, a1: float = None, print_: bool = True) -> float:
        """produce f from a1"""
        factor1 = n * (1 + j) ** (n - 1)
        factor2 = (((1 + i) ** n) - ((1 + j) ** n)) / (i - j)
        if a1:
            if i == j:
                if print_:
                    self.print_factor(factor=factor1,
                                      name=f"(F/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return a1 * factor1
            else:
                if print_:
                    self.print_factor(factor=factor2,
                                      name=f"(F/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return a1 * factor2
        else:
            if i == j:
                if print_:
                    self.print_factor(factor=factor1,
                                      name=f"(F/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return factor1
            else:
                if print_:
                    self.print_factor(factor=factor2,
                                      name=f"(F/A1, {i:.{self.decimal_digits}f}, {j:.{self.decimal_digits}f}, {n})")
                return factor2

    def rg(self, parameters: list, print_: bool = True) -> float:
        """calculate geometric sequence mean"""

        answer = 1
        for i in parameters:
            answer *= (i + 1)
        factor = answer ** (1 / len(parameters)) - 1
        if print_:
            self.print_factor(factor=factor, name=f"(RG)")
        return factor

    def ie(self, r: float, m: int, print_: bool = True) -> float:
        """produce effective interest rate"""
        factor = (1 + r / m) ** m - 1
        if print_:
            self.print_factor(factor=factor, name=f"(ie, r={r:.{self.decimal_digits}f}, m={m})")
        return factor

    def i_from_ie(self, ie: float, m: int, print_: bool = True) -> float:
        """produce interest rate from effective interest rate"""
        factor = (ie + 1) ** (1 / m) - 1
        if print_:
            self.print_factor(factor=factor, name=f"(i_from_ie, ie={ie:.{self.decimal_digits}f}, m={m})")
        return factor


class Continuous_Eco(Eco):
    def __init__(self, decimal_digits: int = 4) -> None:
        super().__init__()
        self.decimal_digits = decimal_digits

    def p_f(self, r: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce p from f"""
        factor = exp(-r * n)
        if print_:
            self.print_factor(factor=factor, name=f"(P/F, r={r:.{self.decimal_digits}f}, n={n})")
        if f:
            return f * factor
        else:
            return factor

    def f_p(self, r: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce f from p"""
        factor = exp(r * n)
        if print_:
            self.print_factor(factor=factor, name=f"(F/P, r={r:.{self.decimal_digits}f}, n={n})")
        if p:
            return p * factor
        else:
            return factor

    def f_a(self, r: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce f from a"""
        factor = (exp(r * n) - 1) / (exp(r) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(F/A, r={r:.{self.decimal_digits}f}, n={n})")
        if a:
            return a * factor
        else:
            return factor

    def a_f(self, r: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce a from f"""
        factor = (exp(r) - 1) / (exp(r * n) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/F, r={r:.{self.decimal_digits}f}, n={n})")
        if f:
            return f * factor
        else:
            return factor

    def p_a(self, r: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce p from a"""
        factor = (exp(r * n) - 1) / (exp(r * n) * (exp(r) - 1))
        if print_:
            self.print_factor(factor=factor, name=f"(P/A, r={r:.{self.decimal_digits}f}, n={n})")
        if a:
            return a * factor
        else:
            return factor

    def a_p(self, r: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce a from p"""
        factor = (exp(r * n) * (exp(r) - 1)) / (exp(r * n) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/P, r={r:.{self.decimal_digits}f}, n={n})")
        if p:
            return p * factor
        else:
            return factor

    def p_g(self, r: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce p from g"""
        factor = (exp(r * n) - 1 - n * (exp(r) - 1)) / (exp(r * n) * ((exp(r) - 1) ** 2))
        if print_:
            self.print_factor(factor=factor, name=f"(P/G, r={r:.{self.decimal_digits}f}, n={n})")
        if g:
            return g * factor
        else:
            return factor

    def a_g(self, r: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce a from g"""
        factor = (1 / (exp(r) - 1)) - (n / (exp(r * n) - 1))
        if print_:
            self.print_factor(factor=factor, name=f"(A/G, r={r:.{self.decimal_digits}f}, n={n})")
        if g:
            return g * factor
        else:
            return factor

    def ie(self, r: float, print_: bool = True) -> float:
        """produce effective interest rate"""
        factor = exp(r) - 1
        if print_:
            self.print_factor(factor=factor, name=f"(ie, r={r:.{self.decimal_digits}f})")
        return factor

    def p_abar(self, r: float, n: int, abar: float = None, print_: bool = True) -> float:
        """produce p from a_bar"""
        factor = (exp(r * n) - 1) / (r * exp(r * n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/A_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if abar:
            return abar * factor
        else:
            return factor

    def p_fbar(self, r: float, n: int, fbar: float = None, print_: bool = True) -> float:
        """produce p from f_bar"""
        factor = (exp(r) - 1) / (r * exp(r * n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/F_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if fbar:
            return fbar * factor
        else:
            return factor

    def f_abar(self, r: float, n: int, abar: float = None, print_: bool = True) -> float:
        """produce f from a_bar"""
        factor = (exp(r * n) - 1) / r
        if print_:
            self.print_factor(factor=factor, name=f"(F/A_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if abar:
            return abar * factor
        else:
            return factor
