def katty(word: str, rep: int) -> None:
    length = len(word)
    main_pattern = list(word * (rep + 1))
    pattern = main_pattern.copy()
    for i in range(length):
        pattern = main_pattern.copy()
        for j in range(i):
            pattern.pop(0)
        for k in range(length - i):
            pattern.pop(len(pattern) - 1)
        print("".join(pattern))           #Keip S


tests = []
while True:
    tests.append(input().split())
    if tests[-1] == ["."]:
        break
for i in range(len(tests) - 1):
    katty(tests[i][0], int(tests[i][1]))
