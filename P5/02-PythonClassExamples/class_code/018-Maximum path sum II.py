from pathlib import Path
file_name = Path("/mnt/Data1/Python_Projects/Pure-Python/P5/02-PythonClassExamples/class_code/p067_triangle.txt")
print(file_name)
file = open(file_name, "r")
List = []

for line in file.readlines():
    line = line[:-1]
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    List.append(line)


def adding(row: list, add: list) -> None:
    for i in range(len(row)):
        row[i] += max(add[i], add[i + 1])


def reduce(tri: list) -> list:
    for i in range(len(tri) - 1, 0, -1):
        adding(tri[i - 1], tri[i])
    return tri[0]


print(reduce(List))


