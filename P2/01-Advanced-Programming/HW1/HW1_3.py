class Decoding:
    def __init__(self, code: str, k: int) -> None:
        self.code = list(code)
        self.decode = []
        self.k = k
        self.step = 1
        self.direction = 1

    def main(self, i=-1) -> str:
        while len(self.decode) < self.k:
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
                if self.direction == 1:
                    self.code.extend(self.code[:i:self.step])
                elif self.direction == -1:
                    self.code.extend(self.code[i + 1::self.step])
            elif self.code[i] == "/":
                if self.direction == 1:
                    self.code[:i] = self.vice_versa(self.code[:i])
                elif self.direction == -1:
                    self.code[i + 1:] = self.vice_versa(self.code[i + 1:])
            else:
                self.decode.append(self.code[i])
        return "".join(self.decode)

    def add(self) -> None:
        self.step += 1

    def mines(self) -> None:
        if self.step != 1:
            self.step -= 1

    def change_dir(self) -> None:
        self.direction *= -1

    @staticmethod
    def vice_versa(s: list) -> list:
        sp = []
        for i in range(len(s) - 1, -1, -1):
            sp.append(s[i])
        return sp


input_str = input()
input_k = int(input())
obj = Decoding(input_str, input_k)
print(obj.main())
