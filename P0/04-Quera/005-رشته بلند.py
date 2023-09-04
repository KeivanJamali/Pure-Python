class Crazy_program:
    def __init__(self, field: str):
        self.main_field = field
        self.worse = 0

    def copy(self, field: str, n: int) -> None:
        field = field * n
        self.main_field = field + self.main_field[len(field):]

    def compare(self, field: str) -> None:
        if field == self.main_field:
            self.worse += 1

    def substr(self, field: str, n: int) -> None:
        length = len(field)
        s = 0
        for i in range(len(self.main_field)):
            if field == self.main_field[i:i + length]:
                s += 1
        if s == n:
            self.worse += 1

    def attach(self, field1: str, n: int, field2: str) -> None:
        n_field = field1 + field2
        self.substr(n_field, n)

    def length(self, n: int) -> None:
        if len(self.main_field) == n:
            self.worse += 1


def main():
    line = input()
    line = Crazy_program(line)
    i = 0

    while True:
        i += 1
        temp = input().split()
        if len(temp) == 2:
            if temp[0] == "length":
                line.length(int(temp[1]))
            else:
                line.compare(temp[1])
        elif len(temp) == 3:
            if temp[0] == "copy":
                line.copy(temp[1], int(temp[2]))
            else:
                line.substr(temp[1], int(temp[2]))
        elif len(temp) == 4:
            line.attach(temp[1], int(temp[2]), temp[3])
        else:
            i -= 1
            if line.worse >= i/2:
                print("Eyval")
                break
            else:
                print("HeifShod")
                break
if __name__ == '__main__':
    main()