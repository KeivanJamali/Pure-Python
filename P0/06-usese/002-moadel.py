class moadel:
    def __init__(self):
        self.m = 0

    def math(self, n: float):
        self.m += n * 4

    def per(self, n: float):
        self.m += n * 3

    def En(self, n: float):
        self.m += n * 3

    def ehtemal(self, n: float):
        self.m += n * 3

    def mabani(self, n: float):
        self.m += n * 3

    def estatic(self, n: float):
        self.m += n * 3

    def az(self, n: float):
        self.m += n

    def __str__(self):
        an = self.m / 20
        return str(an)


result = moadel()
result.math(18.5)
result.per(20.0)
result.En(19.4)
result.ehtemal(20)
result.mabani(20.0)
result.estatic(18.3)
result.az(19.1)
print(result)
