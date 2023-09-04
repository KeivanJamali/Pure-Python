class Soil_U:
    def __init__(self, A200, A4, LL, PI, D10, D30, D60, oven_LL=0):
        """Getting Inputs"""
        self.A200 = A200
        self.A4 = A4
        self.LL = LL
        # self.PL = PL
        self.D10 = D10
        self.D30 = D30
        self.D60 = D60
        self.Cc = (self.D30) ** 2 / (self.D10 * self.D60)
        self.Cu = self.D60 / self.D10
        self.PI = PI
        self.A = self.A_line(LL)
        if oven_LL == False:
            self.oven_LL = LL
        else:
            self.oven_LL = oven_LL

    def __str__(self):
        """finding Soil_Kind"""
        if self.A200 < 50:
            if self.A4 < (100 - self.A200) / 2:  # Gravel
                if self.A200 < 5:
                    if self.Cu >= 4 and self.Cc <= 3 and self.Cc >= 1:  # Well Graded Gravel
                        # print("GW")
                        return "GW"
                    else:  # Poor Graded Gravel
                        # print("GP")
                        return "GP"
                elif self.A200 > 12:
                    if self.PI < 4 or self.PI < self.A:  # Silty Gravel
                        # print("GM")
                        return "GM"
                    elif self.PI > 7 and self.PI >= self.A:  # Clayey Gravel
                        # print("GC")
                        return "GC"
                else:
                    if self.Cu >= 4 and self.Cc <= 3 and self.Cc >= 1:  # Well Graded gravel

                        if self.PI < 4 or self.PI < self.A:  # Silty Sand
                            # print("GW-GM")
                            return "GW-GM"
                        elif self.PI > 7 and self.PI >= self.A:  # Clayey Sand
                            # print("GW-GC")
                            return "GW-GC"
                    else:  # Poor Graded Sand
                        if self.PI < 4 or self.PI < self.A:  # Silty Sand
                            # print("GP-GM")
                            return "GP-GM"
                        elif self.PI > 7 and self.PI >= self.A:  # Clayey Sand
                            # print("GP-GC")
                            return "GP-GC"

            else:  # Sand
                if self.A200 < 50:
                    if self.Cu >= 6 and self.Cc <= 3 and self.Cc >= 1:  # Well Graded Sand
                        # print("SW")
                        return "SW"
                    else:  # Poor Graded Sand
                        # print("SP")
                        return "SP"
                elif self.A200 > 12:
                    if self.PI < 4 or self.PI < self.A:  # Silty Sand
                        # print("SM")
                        return "SM"
                    elif self.PI > 7 and self.PI >= self.A:  # Clayey Sand
                        # print("SC")
                        return "SC"
                else:
                    if self.Cu >= 6 and self.Cc <= 3 and self.Cc >= 1:  # Well Graded Sand
                        if self.PI < 4 or self.PI < self.A:  # Silty Sand
                            # print("SW-SM")
                            return "SW-SM"
                        elif self.PI > 7 and self.PI >= self.A:  # Clayey Sand
                            # print("SW-SC")
                            return "SW-SC"
                    else:  # Poor Graded Sand
                        if self.PI < 4 or self.PI < self.A:  # Silty Sand
                            # print("SP-SM")
                            return "SP-SM"
                        elif self.PI > 7 and self.PI >= self.A:  # Clayey Sand
                            # print("SP-SC")
                            return "SP-SC"
                        elif self.PI < 7 and self.LL < 25 and self.LL > 12:
                            return "SC-SM"
        elif self.A200 > 50:
            if self.LL < 50:
                if self.oven_LL / self.LL < 0.75:  # Organic Low Plasticity
                    # print("OL")
                    return "OL"
                elif self.PI > 7 and self.PI >= self.A:  # Clay Low Plasticity
                    # print("CL")
                    return "CL"
                elif self.PI < 4 or self.PI < self.A:  # Silt Low Plasticity
                    # print("ML")
                    return "ML"
                elif self.PI < 7 and self.LL<25 and self.LL>12:
                    return "CL-ML"
            else:
                if self.oven_LL / self.LL < 0.75:  # Organic High Plasticity
                    # print("OH")
                    return "OH"
                elif self.PI >= self.A:  # Clay High Plasticity

                    # print("CH")
                    return "CH"
                elif self.PI < self.A:  # Silt High Plasticity
                    # print("MH")
                    return "MH"
        else:
            return "GM-ML"
        return "Nothing match!"

    def A_line(self, LL):
        """A_line Function"""
        return 0.73 * (LL - 20)


def Main():
    A200 = int(input("percentage of passing from #200: "))
    A4 = int(input("percentage of passing from #4: "))
    LL = int(input("Liquid Limit: "))
    PI = int(input("Plastic Index: "))
    D10 = int(input("D10: "))
    D30 = int(input("D30: "))
    D60 = int(input("D60: "))
    oven_LL = int(input("Liquid Limit After Oven: "))
    A = Soil_U(A200, A4, LL, PI, D10, D30, D60, oven_LL)
    print(A)


A = Soil_U(60, 100, 30, 22, 12, 7.844, 42.72, 25)
B = Soil_U(10, 60, 24, 5, 5, 19.365, 25)
C = Soil_U(60, 80, 55, 35, 5, 15.811, 25)
D = Soil_U(8 , 70 , 55, 20, 1, 1, 1)
print(A)
print(B)
print(C)
print(D)
