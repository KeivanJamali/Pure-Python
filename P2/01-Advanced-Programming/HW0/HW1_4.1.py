class Fly:
    def __init__(self, n: int, m: int) -> None:
        self.matrix = None
        self.n = n
        self.m = m
        self.make_matrix(n, m)

    def make_matrix(self, n: int, m: int) -> None:
        matrix = []
        for i in range(n):
            input_line = input().split(" ")
            matrix.append(input_line)
        self.matrix = matrix

    def check_fly(self, i, j) -> int:
        count = 0
        for k in range(j + 1, self.m):
            if self.matrix[i][k] == "C":
                break
            if self.matrix[i][k] == "F":
                count += 1
        for k in range(j - 1, -1, -1):
            if self.matrix[i][k] == "C":
                break
            if self.matrix[i][k] == "F":
                count += 1

        for k in range(i + 1, self.n):
            if self.matrix[k][j] == "C":
                break
            if self.matrix[k][j] == "F":
                count += 1
        for k in range(i - 1, -1, -1):
            if self.matrix[k][j] == "C":
                break
            if self.matrix[k][j] == "F":
                count += 1
        return count


def main():
    n, m = input().split(" ")
    n, m = int(n), int(m)
    obj = Fly(n, m)
    max_sum = 0
    for i in range(n):
        for j in range(m):
            if obj.matrix[i][j] == "B":
                new_sum = obj.check_fly(i, j)
                if max_sum < new_sum:
                    max_sum = new_sum
    print(max_sum)


main()
