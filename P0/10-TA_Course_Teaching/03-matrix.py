def transpose(matrix: list) -> list:
    length = len(matrix)
    result_matrix = []
    for i in range(length):
        result_matrix.append([])
    for i in range(length):
        for j in range(length):
            result_matrix[j].append(matrix[i][j])
    return result_matrix


def give_number(matrix: list) -> list:
    result_list = []
    t_matrix = transpose(matrix)
    for i in range(len(matrix)):
        result_list.append(sum(matrix[i]))
    for i in range(len(t_matrix)):
        result_list.append(sum(t_matrix[i]))
    return result_list


def main(matrix: list) -> None:
    numbers = give_number(matrix)
    for i in range(2):
        for j in range(len(matrix)):
            print(numbers.pop(0), end=" ")
        print()


m = [[1, 3], [10, 5]]
main(m)
