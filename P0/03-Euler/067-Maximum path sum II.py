from pathlib import Path
file_name = Path("P0/03-Euler/p067_triangle.txt")
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


i = 0
def max_path_sum_tree(tree):
    global i
    print(f"{i}call")
    i += 1
    if len(tree) == 1:
        return tree[0][0]
    
    left_subtree = [row[:-1] for row in tree[1:]]
    right_subtree = [row[1:] for row in tree[1:]]
    
    left_sum = max_path_sum_tree(left_subtree)
    right_sum = max_path_sum_tree(right_subtree)
    
    return tree[0][0] + max(left_sum, right_sum)

print(max_path_sum_tree(List))
