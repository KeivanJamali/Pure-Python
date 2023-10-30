import pandas as pd


class Fly:
    def __init__(self, n: int, m: int) -> None:
        self.matrix = None
        self.make_matrix(n, m)

    def make_matrix(self, n: int, m: int) -> None:
        matrix = pd.DataFrame(index=range(n), columns=range(m))
        for i in range(n):
            input_line = input().split(" ")
            matrix.iloc[i] = input_line
        self.matrix = matrix

    def check_fly(self, i, j) -> int:
        count = (self.matrix.iloc[i, :] == "F").sum() + (self.matrix.iloc[:, j] == "F").sum()
        return count


def main():
    n, m = input().split(" ")
    obj = Fly(int(n), int(m))
    max_sum = 0
    for i in range(len(obj.matrix)):
        for j in range(len(obj.matrix.columns)):
            if obj.matrix.iloc[i, j] == "B":
                new_sum = obj.check_fly(i, j)
                if max_sum < new_sum:
                    max_sum = new_sum
    print(max_sum)


main()
