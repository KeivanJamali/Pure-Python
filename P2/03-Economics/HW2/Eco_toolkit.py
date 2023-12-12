from math import exp
import matplotlib.pyplot as plt


class Eco:
    def __init__(self):
        self.decimal_digits = 4

    def print_factor(self, factor: float, name: str) -> None:
        print(f"__{name} = {factor:.{self.decimal_digits}f}__")

    def print_result(self, result: list, name: list, time: bool = False) -> None:
        for i in range(len(result)):
            if not time:
                print(f"__$$ {name[i]} = {result[i]:.{self.decimal_digits}f} $$__")
            else:
                time_1 = str(result[i])
                time_1 = time_1.split(".")
                time_2 = result[i] - int(time_1[0])
                time_2 = time_2 * 12
                print(f"__$$ {name[i]} = {int(time_1[0])} year and {time_2:.{self.decimal_digits}f} month $$__")

    @staticmethod
    def visualize(dict_list: list, show: bool = True, title=None, legend: bool = False, scaler: float = 1) -> None:
        for dict_ in dict_list:
            x = []
            y = []
            for key, value in dict_.items():
                x.append(key)
                x.append(key)
                x.append(key)
                y.append(0)
                y.append(value * scaler)
                y.append(0)

            for i in range(1, len(x), 3):
                plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')

            for i in range(1, len(x), 3):
                plt.text(x[i], 0, str(x[i]), ha='center', va='bottom', position=(x[i], -0.8), c="y")
            plt.plot(x, y, label=f"Scenario {dict_list.index(dict_) + 1}")
        if show:
            if title:
                plt.title(title)
            if legend:
                plt.legend()
            plt.show()


class Primary_Eco(Eco):
    def __init__(self, decimal_digits: int = 4):
        super().__init__()
        self.decimal_digits = decimal_digits

    def p_to_f(self, i: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce f from p"""
        factor = (1 + i) ** n
        if print_:
            self.print_factor(factor=factor, name=f"(F/P, {i:.{self.decimal_digits}f}, {n})")
        if p:
            return p * factor
        else:
            return factor

    def f_to_p(self, i: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce p from f"""
        factor = 1 / (1 + i) ** n
        if print_:
            self.print_factor(factor=factor, name=f"(P/F, {i:.{self.decimal_digits}f}, {n})")
        if f:
            return f * factor
        else:
            return factor

    def a_to_p(self, i: float, n: int = None, a: float = None, print_: bool = True) -> float:
        """produce p from a"""
        if n:
            factor = ((1 + i) ** n - 1) / ((1 + i) ** n * i)
            if print_:
                self.print_factor(factor=factor, name=f"(P/A, {i:.{self.decimal_digits}f}, {n})")
            if a:
                return a * factor
            else:
                return factor
        else:
            factor = 1 / i
            if print_:
                self.print_factor(factor=factor, name=f"(P/A for inf years, {i:.{self.decimal_digits}f})")
            if a:
                return a * factor
            else:
                return factor

    def p_to_a(self, i: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce a from p"""
        factor = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/P, {i:.{self.decimal_digits}f}, {n})")
        if p:
            return p * factor
        else:
            return factor

    def a_to_f(self, i: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce f from a"""
        factor = ((1 + i) ** n - 1) / i
        if print_:
            self.print_factor(factor=factor, name=f"(F/A, {i:.{self.decimal_digits}f}, {n})")
        if a:
            return a * factor
        else:
            return factor

    def f_to_a(self, i: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce a from f"""
        factor = i / ((1 + i) ** n - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/F, {i:.{self.decimal_digits}f}, {n})")
        if f:
            return f * factor
        else:
            return factor

    def g_to_p(self, i: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce p from g"""
        factor = (1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/G, {i:.{self.decimal_digits}f}, {n})")
        if g:
            return g * factor
        else:
            return factor

    def g_to_a(self, i: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce a from g"""
        factor = (1 / i) - (n / (((1 + i) ** n) - 1))
        if print_:
            self.print_factor(factor=factor, name=f"(A/G, {i:.{self.decimal_digits}f}, {n})")
        if g:
            return g * factor
        else:
            return factor

    def a1_to_p(self, i: float, j: float, n: int, a1: float = None, print_: bool = True) -> float:
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

    def a1_to_f(self, i: float, j: float, n: int, a1: float = None, print_: bool = True) -> float:
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

    def some_f_to_p(self, i: float, all_f: list) -> float:
        """produce p from some a"""
        result = 0
        for iteration in range(len(all_f)):
            p = Primary_Eco().f_to_p(i=i, n=iteration + 1, f=all_f[iteration], print_=False)
            result += p
        return result


class Continuous_Eco(Eco):
    def __init__(self, decimal_digits: int = 4) -> None:
        super().__init__()
        self.decimal_digits = decimal_digits

    def f_to_p(self, r: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce p from f"""
        factor = exp(-r * n)
        if print_:
            self.print_factor(factor=factor, name=f"(P/F, r={r:.{self.decimal_digits}f}, n={n})")
        if f:
            return f * factor
        else:
            return factor

    def p_to_f(self, r: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce f from p"""
        factor = exp(r * n)
        if print_:
            self.print_factor(factor=factor, name=f"(F/P, r={r:.{self.decimal_digits}f}, n={n})")
        if p:
            return p * factor
        else:
            return factor

    def a_to_f(self, r: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce f from a"""
        factor = (exp(r * n) - 1) / (exp(r) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(F/A, r={r:.{self.decimal_digits}f}, n={n})")
        if a:
            return a * factor
        else:
            return factor

    def f_to_a(self, r: float, n: int, f: float = None, print_: bool = True) -> float:
        """produce a from f"""
        factor = (exp(r) - 1) / (exp(r * n) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/F, r={r:.{self.decimal_digits}f}, n={n})")
        if f:
            return f * factor
        else:
            return factor

    def a_to_p(self, r: float, n: int, a: float = None, print_: bool = True) -> float:
        """produce p from a"""
        factor = (exp(r * n) - 1) / (exp(r * n) * (exp(r) - 1))
        if print_:
            self.print_factor(factor=factor, name=f"(P/A, r={r:.{self.decimal_digits}f}, n={n})")
        if a:
            return a * factor
        else:
            return factor

    def p_to_a(self, r: float, n: int, p: float = None, print_: bool = True) -> float:
        """produce a from p"""
        factor = (exp(r * n) * (exp(r) - 1)) / (exp(r * n) - 1)
        if print_:
            self.print_factor(factor=factor, name=f"(A/P, r={r:.{self.decimal_digits}f}, n={n})")
        if p:
            return p * factor
        else:
            return factor

    def g_to_p(self, r: float, n: int, g: float = None, print_: bool = True) -> float:
        """produce p from g"""
        factor = (exp(r * n) - 1 - n * (exp(r) - 1)) / (exp(r * n) * ((exp(r) - 1) ** 2))
        if print_:
            self.print_factor(factor=factor, name=f"(P/G, r={r:.{self.decimal_digits}f}, n={n})")
        if g:
            return g * factor
        else:
            return factor

    def g_to_a(self, r: float, n: int, g: float = None, print_: bool = True) -> float:
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

    def abar_to_p(self, r: float, n: int, abar: float = None, print_: bool = True) -> float:
        """produce p from a_bar"""
        factor = (exp(r * n) - 1) / (r * exp(r * n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/A_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if abar:
            return abar * factor
        else:
            return factor

    def fbar_to_p(self, r: float, n: int, fbar: float = None, print_: bool = True) -> float:
        """produce p from f_bar"""
        factor = (exp(r) - 1) / (r * exp(r * n))
        if print_:
            self.print_factor(factor=factor, name=f"(P/F_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if fbar:
            return fbar * factor
        else:
            return factor

    def abar_to_f(self, r: float, n: int, abar: float = None, print_: bool = True) -> float:
        """produce f from a_bar"""
        factor = (exp(r * n) - 1) / r
        if print_:
            self.print_factor(factor=factor, name=f"(F/A_bar, r={r:.{self.decimal_digits}f}, n={n})")
        if abar:
            return abar * factor
        else:
            return factor


class My_Eco(Eco):
    def __init__(self, decimal_digits: int = 4):
        super().__init__()
        self.decimal_digits = decimal_digits
