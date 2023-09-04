def mat_beauty(matrix: list) -> list:
    temp = matrix.copy()
    for i in range(0, len(temp) - 1, 2):
        if temp[i] >= 0 and temp[i + 1] >= 0:
            matrix[i] = temp[i] + temp[i + 1]
            matrix[i + 1] = 0
        if temp[i] <= 0 and temp[i + 1] <= 0:
            matrix[i] = temp[i] + temp[i + 1]
            matrix[i + 1] = 0
    try:
        while True:
            matrix.remove(0)         #Keip S
    except:
        return matrix


def max_sum_s(matrix: list) -> int:
    max_sum = 0
    length = len(matrix)
    for i in range(length):
        for j in range(i, length):
            temp = sum(matrix[i:j + 1])
            if max_sum < temp:
                max_sum = temp      #Keip S
    return max_sum


n_test = int(input())
answers = []
for i in range(n_test):
    n_variable = int(input())
    my_matrix = input().split()
    for i in range(len(my_matrix)):
        my_matrix[i] = int(my_matrix[i])
    answers.append(max_sum_s(my_matrix))
for i in answers:
    print(i)
