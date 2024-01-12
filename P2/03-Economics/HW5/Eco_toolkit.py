from math import exp
import matplotlib.pyplot as plt
import numpy as np


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

    def table(self, approach: str, **kwargs) -> None:
        if approach == "BV":
            print(f"--------------------------  TABLE   --------------------------")
            print(f"Year  ------    Dj   --------------   BV   ----------")
            print(f" {0:.0f}     |      {0:.2f}      |      {kwargs['bv'][0]:.2f} ")
            for i in range(kwargs["n"]):
                print(f" {i + 1:.0f}     |      {kwargs['dj'][i]:.2f}      |      {kwargs['bv'][i + 1]:.2f} ")
            print(f"--------------------------   END    --------------------------")
        elif approach == "SL":
            print(f"--------------------------  TABLE   --------------------------")
            print(f"Year  ------  Dj   --------------   SL   ---------")
            for i in range(kwargs["n"]):
                print(f" {i:.0f}     |      {kwargs['dj'][i]:.2f}      |      {kwargs['sl'][i]:.2f} ")
            print(f"--------------------------   END    --------------------------")
        elif approach == "TAX":
            print(f"--------------------------  TABLE   --------------------------")
            print(
                f"Year  ------  CFBT   --------------   Dj   --------------   TI   --------------   TAX   --------------   CFAT   ----------")
            for i in range(kwargs["n"]):
                print(
                    f" {i:.0f}     |      {kwargs['cfbt'][i]:.2f}      |      {kwargs['dj'][i]:.2f}      |      {kwargs['ti'][i]:.2f}      |      {kwargs['tax'][i]:.2f}      |      {kwargs['cfat'][i]:.2f}")
            print(f"--------------------------   END    --------------------------")

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

    def some_f_to_p(self, i: float, all_f: list, with_p: bool = True) -> float:
        """produce p from some a"""
        all_f_copy = all_f.copy()
        if with_p:
            result = all_f_copy.pop(0)
        else:
            result = 0

        for iteration in range(len(all_f_copy)):
            primary = Primary_Eco()
            p = primary.f_to_p(i=i, n=iteration + 1, f=all_f_copy[iteration], print_=False)
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


class Equation_Eco(Eco):
    def __init__(self, decimal_digits: int = 4):
        super().__init__()
        self.decimal_digits = decimal_digits
        self.math = ["+", "-", "*", "^", "/", "="]

    def plot_eq_to_solve(self, equ, error: float = 50, print_: bool = True, plot: bool = False):
        """send the function of lambda x. 0=equation"""
        results = []
        x = []
        for i in np.arange(0.001, 1, 0.001):
            s = equ(i)
            if abs(s) < error:
                results.append(s)
                x.append(i)

        if plot:
            plt.plot(x, results, c="b")
            plt.plot(x, np.zeros(len(x)), c="r")
            plt.show()

        solution_final = np.average(x)
        if print_:
            self.print_factor(factor=solution_final, name=f"ROR")
        return x


class Tax_Eco(Eco):
    def __init__(self, decimal_digits: int = 4):
        super().__init__()
        self.decimal_digits = decimal_digits

    def sl(self, p: float, sv: float, n: int, print_: bool = True) -> tuple:
        """produce sl, [ (p-sv)/2=n ]"""
        dj = [(p - sv) / n for _ in range(n)]
        bv = [p]

        for i in range(n):
            bv.append(bv[i] - dj[i])

        if print_:
            self.table(approach="BV", n=n, dj=dj, bv=bv)

        dj.insert(0, 0)
        return dj, bv

    def soyd(self, p: float, sv: float, n: int, print_: bool = True) -> tuple:
        """produce SOYD [ (n-(j-1))/(n*(n+1)/2) ]"""
        dj = []
        bv = [p]
        for j in range(1, n + 1):
            dj.append(((n - (j - 1)) / ((n * (n + 1)) / 2)) * (p - sv))
            bv.append(bv[j - 1] - dj[j - 1])
        if print_:
            self.table(approach="BV", n=n, dj=dj, bv=bv)
        dj.insert(0, 0)
        return dj, bv

    def db(self, p: float, n: int, approach: str, f: float = None, sv: float = None, print_: bool = True,
           dont: str = False) -> tuple:
        """produce DDB [ (n-1)/(n*(n+1)/2) ]
        approach = [factor, sv, ddb
        3 possibilities:
            1: we have f: question gives us [d%].
            2: we don't have [d%] but we have [sv](Declining inventory method).
            3: we don't have [amortization factor] and [sv] but the method is DDB(double declining inventory method)."""
        dj = []
        bv = [p]

        if approach == "one":
            f = f
        elif approach == "two":
            f = 1 - (sv / p) ** (1 / n)
        elif approach == "ddb":
            f = 2 / n

        for j in range(1, n + 1):
            dj.append(p * f * ((1 - f) ** (j - 1)))
            bv.append(bv[j - 1] - dj[j - 1])

        if print_:
            print("first:")
            self.table(approach="BV", n=n, dj=dj, bv=bv)

        if not dont:
            if bv[-1] < sv:
                for i in range(len(bv)):
                    if bv[i] < sv:
                        bv[i] = sv
                        dj[i - 1] = bv[i - 1] - sv
                if print_:
                    print("BV_last is smaller than SV... easy!")
                    self.table(approach="BV", n=n, dj=dj, bv=bv)

            elif bv[-1] > sv:
                sl = []
                for j in range(n):
                    sl.append((bv[j] - sv) / (n - ((j + 1) - 1)))
                for i in range(len(sl)):
                    if sl[i] > dj[i]:
                        index, new = i, sl[i]
                        break
                for i in range(len(dj)):
                    if i >= index:
                        dj[i] = new
                        bv[i + 1] = bv[i] - new
                if print_:
                    print("BV_last is larger than SV... Too bad!")
                    self.table(approach="SL", n=n, dj=dj, sl=sl)
                    self.table(approach="BV", n=n, dj=dj, bv=bv)
        dj.insert(0, 0)
        return dj, bv

    def cfat(self, cfbt: list, dj: list, tax_rate: float, print_: bool = True) -> list:
        """calculate CFAT"""
        cfat = []
        ti = []
        tax = []
        for i in range(len(cfbt)):
            ti_temp = cfbt[i] - dj[i]
            ti.append(0) if ti_temp < 0 else ti.append(ti_temp)
            tax.append(ti[i] * tax_rate)
            cfat.append(cfbt[i] - tax[i])

        if print_:
            self.table(approach="TAX", n=len(cfbt), cfbt=cfbt, dj=dj, ti=ti, tax=tax, cfat=cfat)

        return cfat
