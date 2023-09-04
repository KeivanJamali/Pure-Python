class Soil_A:
    def __init__(self, A10, A40, A200, LL, PI):
        self.A10 = A10
        self.A40 = A40
        self.A200 = A200
        self.LL = LL
        self.PI = PI

    def __str__(self):
        ans = self.Find_GI()
        if self.A10 <= 50 and self.A40 <= 30 and self.A200 <= 15 and self.PI <= 6:
            return f"A-1-a({ans})"
        elif self.A40 <= 50 and self.A200 <= 25 and self.PI <= 6:
            return f"A-1-b({ans})"
        elif self.A40 > 50 and self.A200 <= 10:
            return f"A-3({ans})"
        elif self.A200 <= 35 and self.LL <= 40 and self.PI <= 10:
            return f"A-2-4({ans})"
        elif self.A200 <= 35 and self.LL > 40 and self.PI <= 10:
            return f"A-2-5({ans})"
        elif self.A200 <= 35 and self.LL >= 40 and self.PI > 10:
            return f"A-2-6({ans})"
        elif self.A200 <= 35 and self.LL > 40 and self.PI > 10:
            return f"A-2-7({ans})"
        elif self.A200 > 35 and self.LL <= 40 and self.PI <= 10:
            return f"A-4({ans})"
        elif self.A200 > 35 and self.LL > 40 and self.PI <= 10:
            return f"A-5({ans})"
        elif self.A200 > 35 and self.LL <= 40 and self.PI > 10:
            return f"A-6({ans})"
        elif self.A200 > 35 and self.LL > 40 and self.PI > 10:
            if self.PI <= self.LL - 30:
                return f"A-7-5({ans})"
            else:
                return f"A-7-6({ans})"
        else:
            return "no"

    def Find_GI(self):
        if self.A200 > 35:
            GI = (self.A200 - 35) * (0.2 + 0.005 * (self.LL - 40)) + 0.01 * (self.A200 - 15) * (self.PI - 10)
        else:
            GI = 0.01 * (self.A200 - 15) * (self.PI - 10)
        if GI >= 0:
            return round(GI)
        else:
            return 0

    def __round__(self, n):
        if (n * 10) % 10 >= 5:
            return ((n * 10) // 10) + 1
        else:
            return (n * 10) // 10


A = Soil_A(42, 35, 20, 25, 5)

print(A)
