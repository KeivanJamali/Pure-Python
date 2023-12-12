import numpy as np
import matplotlib.pyplot as plt


def p_to_a(i: float, n: int, p: float = None) -> float:
    """produce a from p"""
    factor = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
    if p:
        return p * factor
    else:
        return factor


def f_to_a(i: float, n: int, f: float = None) -> float:
    """produce a from f"""
    factor = i / ((1 + i) ** n - 1)
    if f:
        return f * factor
    else:
        return factor


def print_result(result: list, name: list, time: bool = False) -> None:
    for i in range(len(result)):
        if not time:
            print(f"__$$ {name[i]} = {result[i]:.{4}f} $$__")
        else:
            time_1 = str(result[i])
            time_1 = time_1.split(".")
            time_2 = result[i] - int(time_1[0])
            time_2 = time_2 * 12
            print(f"__$$ {name[i]} = {int(time_1[0])} year and {time_2:.{4}f} month $$__")


def a_to_p(i: float, n: int = None, a: float = None) -> float:
    """produce p from a"""
    if n:
        factor = ((1 + i) ** n - 1) / ((1 + i) ** n * i)
        if a:
            return a * factor
        else:
            return factor
    else:
        factor = 1 / i
        if a:
            return a * factor
        else:
            return factor


def f_to_p(i: float, n: int, f: float = None) -> float:
    """produce p from f"""
    factor = 1 / (1 + i) ** n
    if f:
        return f * factor
    else:
        return factor


def plot_eq_to_solve(equ, plot: bool = True):
    results = []
    x = []
    solution = []
    for i in np.arange(0.001, 1, 0.001):
        s = equ(i)
        if abs(s) < 50:
            results.append(s)
            x.append(i)

    if plot:
        plt.plot(x, results, c="b")
        plt.plot(x, np.zeros(len(x)), c="r")
        plt.show()

    for i in range(len(results)):
        if abs(results[i]) < 5:
            solution.append(x[i])
    solution_final = np.average(solution)
    return solution_final


# question 1
print("........................Start Question 1........................")
i = 0.1
NAW_A = p_to_a(i=i, n=3, p=3000) + 500 - f_to_a(i=i, n=3, f=1000)
NAW_B = p_to_a(i=i, n=6, p=6000) + 600 - f_to_a(i=i, n=6, f=2000)
print_result([NAW_A, NAW_B], ["A", "B"])
print(f"A = {NAW_A:.2f} is better.")

# question 2
print("........................Start Question 2........................")
marr = 0.15
NPW_A = lambda x: -1000 + a_to_p(i=x, n=2, a=450) + f_to_p(i=x, n=3, f=550)
ROR_A = plot_eq_to_solve(NPW_A, plot=False)
print(f"ROR for A is {ROR_A:.2%}")

NPW_B = lambda x: -1800 + a_to_p(i=x, n=2, a=800) + f_to_p(i=x, n=3, f=850)
ROR_B = plot_eq_to_solve(NPW_B, plot=False)
print(f"ROR for B is {ROR_B:.2%}")

NPW_C = lambda x: -4100 + a_to_p(i=x, n=2, a=1800) + f_to_p(i=x, n=3, f=2000)
ROR_C = plot_eq_to_solve(NPW_C, plot=False)
print(f"ROR for C is {ROR_C:.2%}")

NPW_A_B = lambda x: 800 + a_to_p(i=x, n=2, a=-350) + f_to_p(i=x, n=3, f=-300)
ROR_A_B = plot_eq_to_solve(NPW_A_B, plot=False)
print(f"delta ROR for A-B is {ROR_A_B:.2%}")

NPW_B_C = lambda x: 2300 + a_to_p(i=x, n=2, a=-1000) + f_to_p(i=x, n=3, f=-1150)
ROR_B_C = plot_eq_to_solve(NPW_B_C, plot=False)
print(f"delta ROR for B-C is {ROR_B_C:.2%}")

print("C is the best option.")

# question 3
print("........................Start Question 3........................")
i = 0.1

B_S1 = 500
C_S1 = 90 + p_to_a(i=i, n=10, p=3000) - f_to_a(i=i, n=10, f=150)
answer_A = B_S1 / C_S1
print_result([B_S1, C_S1, answer_A], ["B", "C", "resultA"])

B_S2 = 400
C_S2 = 90 + p_to_a(i=i, n=10, p=1000) - f_to_a(i=i, n=10, f=120)
answer_B = B_S2 / C_S2
print_result([B_S2, C_S2, answer_B], ["B", "C", "resultB"])

B_S3 = 440
C_S3 = 80 + p_to_a(i=i, n=10, p=1600) - f_to_a(i=i, n=10, f=100)
answer_C = B_S3 / C_S3
print_result([B_S3, C_S3, answer_C], ["B", "C", "resultC"])

answer_C_B = (B_S3 - B_S2) / (C_S3 - C_S2)
print_result([B_S3 - B_S2, C_S3 - C_S2, answer_C_B], ["B", "C", "result-final"])

print("So C is the best option.")