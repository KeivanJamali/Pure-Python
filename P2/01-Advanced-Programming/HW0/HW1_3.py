english = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
           "L", "l", "M", "04-Project management", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v",
           "W", "w", "X", "x", "Y", "y", "Z", "z"]


class Decoding:
    def __init__(self, code: str) -> None:
        self.code = list(code)
        self.decode = []
        self.step = 1
        self.direction = 1

    def main(self, k: int) -> str:
        i = -1
        while len(self.decode) < k:
            i += self.step * self.direction
            if i > len(self.code) - 1:
                i -= len(self.code)
            elif i < 0:
                i += len(self.code)

            if self.code[i] == "+":
                self.add()
            elif self.code[i] == "-":
                self.mines()
            elif self.code[i] == "!":
                self.change_dir()
            elif self.code[i] == "*":
                self.multi(i)
            elif self.code[i] == "/":
                self.divide(i)
            elif self.code[i] in english:
                self.decode.append(self.code[i])
        return "".join(self.decode)

    def step(self):
        i += self.step * self.direction
        if i > len(self.code) - 1:
            i -= len(self.code)
        elif i < 0:
            i += len(self.code)

    def add(self) -> None:
        self.step += 1

    def mines(self) -> None:
        if self.step > 1:
            self.step -= 1

    def change_dir(self) -> None:
        self.direction *= -1

    def multi(self, i: int) -> None:
        if self.direction == 1:
            self.code.extend(self.code[:i:abs(self.step)])
        elif self.direction == -1:
            self.code.extend(self.code[i + 1::abs(self.step)])

    def divide(self, i: int) -> None:
        if self.direction == 1:
            self.code[:i] = self.vice_versa(self.code[:i])
        elif self.direction == -1:
            self.code[i + 1:] = self.vice_versa(self.code[i + 1:])

    @staticmethod
    def vice_versa(s: list) -> list:
        sp = []
        for i in range(len(s) - 1, -1, -1):
            sp.append(s[i])
        return sp


input_str = input()
input_k = int(input())
obj = Decoding(input_str)
print(obj.main(input_k))
