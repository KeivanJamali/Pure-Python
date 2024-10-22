from itertools import permutations

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
result = []
eq = []
for equation in permutations(digits, 9):
    if int("".join(equation[:2])) * int("".join(equation[2:5])) == int("".join(equation[5:])):
        if not int("".join(equation[5:])) in eq:
            eq.append(int("".join(equation[5:])))
            result.append("".join(equation[:2]) + " X " + "".join(equation[2:5]) + " = " + "".join(equation[5:]))

    if int("".join(equation[:1])) * int("".join(equation[1:5])) == int("".join(equation[5:])):
        if not int("".join(equation[5:])) in eq:
            eq.append(int("".join(equation[5:])))
            result.append("".join(equation[:1]) + " X " + "".join(equation[1:5]) + " = " + "".join(equation[5:]))

print(result)
print(sum(eq))
