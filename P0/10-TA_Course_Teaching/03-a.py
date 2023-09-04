def traspose(matrix: list) -> list:
    length = len(matrix)
    result = []
    for i in range(length):
        result.append([])
    for i in range(length):
        for j in range(length):
            result[j].append(matrix[i][j])
    return result

def give_number(matrix: list) -> list:
    result = []
    for i in matrix:
        result.append(sum(i))
    t_matrix = traspose(matrix)
    for i in t_matrix:
        result.append(sum(i))
    return result


def main(matrix: list) -> None:
    numbers = give_number(matrix)
    for j in range(2):
        for i in range(len(matrix)):
            print(numbers.pop(0), end=" ")
        print()

main([[1, 2, 3], [4, 5, 6], [70, 20, 10]])