import pandas as pd
import numpy as np
from modular.Tables import Tables
import modular.config as config
from math import ceil, pi

class Calculate:
    def __init__(self, Hs):
        self._store_tables()
        self.data = {}
        H = 1.1
        self.d1 = self.find_in_table1(Hs=Hs, H=H)
        self.d2 = self.find_in_table2(Hs=Hs)
        self.d3 = self.find_in_table3(H=H)
        self.apply_table2(self.find_in_table2(Hs=Hs))

        for k, v in self.data.items():
            self.data[k] = str(v)

    def _store_tables(self):
        table = Tables()
        if config.n == 1:
            self.t1 = table.one_table
            self.t2 = table.full_table
            self.t3 = table.bal_table

    def find_in_table1(self, Hs:float, H:float) -> pd.Series:
        t1 = self.t1
        mask_temp_1 = t1["n"] == config.n
        mask_temp_2 = t1["D"] == config.D
        mask_temp_3 = t1["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t1[mask]
        choice = choice[choice["H"] > H].min(axis=0)
        if np.isnan(choice[0]):
            print(f"[Wrong] There is no such {config.n} and {config.D} and {H} and {Hs} in the table.\nYou can change the Hs or you can change the D and try again.")
            return "DONE_E"
        else:
            print("f[INFO] Successfuly find parameters in the table 1.")
            return choice
        
    def find_in_table2(self, Hs:float) -> pd.Series:
        t2 = self.t2
        mask_temp_1 = t2["n"] == config.n
        mask_temp_2 = t2["D"] == config.D
        mask_temp_3 = t2["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t2[mask]
        return choice.iloc[0, :]
    
    def find_in_table3(self, H:float) -> pd.Series:
        t3 = self.t3
        mask = t3["h"]==H
        choice = t3[mask]
        return choice
    
    def apply_table1(self):
        pass

    def apply_table2(self, d:pd.Series):
        self.data["i-001"] = d["p1_diameter(mm)"]
        self.data["i-002"] = Calculate.count_in_pos(1, d["p1_n"])
        self.data["i-003"] = d["p1_sh_i1"]
        self.data["i-004"] = d["p1_sh_i2"]
        self.data["i-005"] = d["p1_sh_i3"]
        self.data["i-006"] = d["p1_sh_i4"]
        self.data["i-007"] = d["p1_sh_i1"]
        self.data["i-008"] = round(float(d["p1_L(m)"]), 1)
        self.data["i-009"] = round(float(d["p1_L(m)"])*float(Calculate.count_in_pos(1, d["p1_n"], cal=True)), 2)
        self.data["i-010"] = Calculate.weight_in_pos(d["p1_diameter(mm)"], dec=3)
        self.data["i-011"] = Calculate.weight_in_pos(d["p1_diameter(mm)"], config.L, 2) 
        self.data["i-012"] = d["p2_diameter(mm)"]
        self.data["i-013"] = Calculate.count_in_pos(2, d["p2_n"])
        self.data["i-014"] = d["p2_sh_i1"]
        self.data["i-015"] = d["p2_sh_i2"]
        self.data["i-016"] = d["p2_sh_i3"]
        self.data["i-017"] = d["p2_sh_i4"]
        self.data["i-018"] = d["p2_sh_i1"]
        self.data["i-019"] = round(float(d["p2_L(m)"]), 1)
        self.data["i-020"] = round(float(d["p1_L(m)"])*float(Calculate.count_in_pos(1, d["p2_n"], cal=True)), 2)
        self.data["i-021"] = Calculate.weight_in_pos(d["p2_diameter(mm)"], dec=3)
        self.data["i-022"] = Calculate.weight_in_pos(d["p2_diameter(mm)"], config.L, 2)
        self.data["i-023"] = d["p3_diameter(mm)"]
        self.data["i-024"] = Calculate.count_in_pos(3, d["p3_n"])
        self.data["i-025"] = d["p3_sh_i1"]
        self.data["i-026"] = Calculate.lengh_in_pos(d["p3_diameter(mm)"])
        self.data["i-027"] = Calculate.lengh_in_pos(d["p3_diameter(mm)"], float(Calculate.count_in_pos(3, d["p3_n"], cal=True)), 2)
        self.data["i-028"] = Calculate.weight_in_pos(d["p3_diameter(mm)"], dec=3)
        self.data["i-029"] = Calculate.weight_in_pos(d["p3_diameter(mm)"], config.L, 2)
        self.data["i-030"] = d["p4_diameter(mm)"]
        self.data["i-031"] = Calculate.count_in_pos(4, d["p4_n"])
        self.data["i-032"] = d["p4_sh_i1"]
        self.data["i-033"] = d["p4_sh_i2"]
        self.data["i-034"] = d["p4_sh_i1"]
        self.data["i-035"] = round(float(d["p4_L(m)"]), 1)
        self.data["i-036"] = round(float(d["p4_L(m)"])*float(Calculate.count_in_pos(4, d["p4_n"], cal=True)), 2)
        self.data["i-037"] = Calculate.weight_in_pos(d["p4_diameter(mm)"], dec=3)
        self.data["i-038"] = Calculate.weight_in_pos(d["p4_diameter(mm)"], config.L, 2)
        self.data["i-039"] = d["p5_diameter(mm)"]
        self.data["i-040"] = Calculate.count_in_pos(5, d["p5_n"])
        self.data["i-041"] = d["p5_sh_i1"]
        self.data["i-042"] = Calculate.lengh_in_pos(d["p5_diameter(mm)"])
        self.data["i-043"] = Calculate.lengh_in_pos(d["p5_diameter(mm)"], float(Calculate.count_in_pos(5, d["p5_n"], cal=True)), 2)
        self.data["i-044"] = Calculate.weight_in_pos(d["p5_diameter(mm)"], dec=3)
        self.data["i-045"] = Calculate.weight_in_pos(d["p5_diameter(mm)"], config.L, 2)
        self.data["i-046"] = d["p6_diameter(mm)"]
        self.data["i-047"] = Calculate.count_in_pos(6, d["p6_n"])
        self.data["i-048"] = d["p6_sh_i1"]
        self.data["i-049"] = Calculate.lengh_in_pos(d["p6_diameter(mm)"])
        self.data["i-050"] = Calculate.lengh_in_pos(d["p6_diameter(mm)"], float(Calculate.count_in_pos(6, d["p6_n"], cal=True)), 2)
        self.data["i-051"] = Calculate.weight_in_pos(d["p6_diameter(mm)"], dec=3)
        self.data["i-052"] = Calculate.weight_in_pos(d["p6_diameter(mm)"], config.L, 2)
        self.data["i-053"] = d["p7_diameter(mm)"]
        self.data["i-054"] = Calculate.count_in_pos(7, d["p7_n"])
        self.data["i-055"] = d["p7_sh_i1"]
        self.data["i-056"] = d["p7_sh_i2"]
        self.data["i-057"] = d["p7_sh_i3"]
        self.data["i-058"] = d["p7_sh_i4"]
        self.data["i-059"] = round(float(d["p7_L(m)"]))
        self.data["i-060"] = round(float(d["p7_L(m)"])*float(Calculate.count_in_pos(7, d["p7_n"], cal=True)), 2)
        self.data["i-061"] = Calculate.weight_in_pos(d["p7_diameter(mm)"], dec=3)
        self.data["i-062"] = Calculate.weight_in_pos(d["p7_diameter(mm)"], config.L, 2)
        self.data["i-063"] = d["p8_diameter(mm)"]
        self.data["i-064"] = Calculate.count_in_pos(8, d["p8_n"])
        self.data["i-065"] = d["p8_sh_i1"]
        self.data["i-066"] = round(float(d["p8_L(m)"]))
        self.data["i-067"] = round(float(d["p8_L(m)"])*float(Calculate.count_in_pos(8, d["p8_n"], cal=True)), 2)
        self.data["i-068"] = Calculate.weight_in_pos(d["p8_diameter(mm)"], dec=3)
        self.data["i-069"] = Calculate.weight_in_pos(d["p8_diameter(mm)"], config.L, 2)
        self.data["i-070"] = d["p9_diameter(mm)"]
        self.data["i-071"] = Calculate.count_in_pos(9, d["p9_n"])
        self.data["i-072"] = d["p9_sh_i1"]
        self.data["i-073"] = d["p9_sh_i2"]
        self.data["i-074"] = d["p9_sh_i3"]
        self.data["i-075"] = d["p9_sh_i4"]
        self.data["i-076"] = d["p9_sh_i5"]
        self.data["i-077"] = round(float(d["p9_L(m)"]))
        self.data["i-078"] = round(float(d["p9_L(m)"])*float(Calculate.count_in_pos(9, d["p9_n"], cal=True)), 2)
        self.data["i-079"] = Calculate.weight_in_pos(d["p9_diameter(mm)"], dec=3)
        self.data["i-080"] = Calculate.weight_in_pos(d["p9_diameter(mm)"], config.L, 2)
        self.data["i-081"] = d["p0_diameter(mm)"]
        self.data["i-082"] = Calculate.count_in_pos(10, d["p0_n"])
        if self.data["i-082"] != "-":
            self.data["i-083"] = d["p0_sh_i1"] + " / " + d["p0_sh_i2"]
            self.data["i-084"] = d["p0_sh_i3"]
            self.data["i-085"] = round(float(d["p1_L(m)"]))
            self.data["i-086"] = round(float(d["p1_L(m)"])*float(Calculate.count_in_pos(10, d["p0_n"], cal=True)), 2)
            self.data["i-087"] = Calculate.weight_in_pos(d["p0_diameter(mm)"], dec=3)
            self.data["i-088"] = Calculate.weight_in_pos(d["p0_diameter(mm)"], config.L, 1) if Calculate.weight_in_pos(d["p0_diameter(mm)"], dec=1) != "-" else "-"
        else:
            self.data["i-083"] = "-"
            self.data["i-084"] = "-"
            self.data["i-085"] = "-"
            self.data["i-086"] = "-"
            self.data["i-087"] = "-"
            self.data["i-088"] = "-"
        c1 = [self.data["i-011"], self.data["i-022"], self.data["i-029"], self.data["i-038"], self.data["i-045"], self.data["i-052"], self.data["i-062"], self.data["i-088"]] 
        c2 = [self.data["i-069"], self.data["i-080"]]
        c3 = [self.data["i-011"], self.data["i-022"], self.data["i-029"], self.data["i-038"], self.data["i-045"], self.data["i-052"], self.data["i-062"], self.data["i-088"], self.data["i-069"], self.data["i-080"]]
        c = [c1, c2, c3]
        c_temp = [[], [], []]
        for i in range(3):
            for j in c[i]:
                if not j == "-":
                    c_temp[i].append(j)
        # print(c_temp[0])
        self.data["i-089"] = round(sum([float(i) for i in c_temp[0]]) / config.L, 1)
        self.data["i-090"] = round(sum([float(i) for i in c_temp[1]]), 1)
        self.data["i-091"] = round(sum([float(i) for i in c_temp[2]]), 1)

    def apply_table3(self):
        pass

    @staticmethod
    def count_in_pos(p:int, count:str, cal=False):
        if count == "-":
            return "-"
        else:
            try:
                count_p1, count_p2 = count.split("*")
            except:
                count_p1, count_p2 = count, None
            if p in [1, 2, 4, 7, 10]:
                res = config.L * float(count_p1)
                if count_p2:
                    if cal:
                        return str(ceil(res) * int(count_p2))
                    else:
                        return str(ceil(res)) + "*" + count_p2
                else:
                    return str(ceil(res))
            else:
                if count_p2:
                    if cal:
                        return str(ceil(float(count_p1)) * int(count_p2))
                    else:
                        return str(ceil(float(count_p1))) + "*" + count_p2
                else:
                    return str(ceil(float(count_p1)))
        
    @staticmethod
    def weight_in_pos(D:float, L:float=None, dec:int=1) -> float:
        if D == "-":
            return "-"
        else:
            if L:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res*L, dec)
            else:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res, dec)
    
    @staticmethod
    def lengh_in_pos(D:float, N:float=None, dec=1) -> float:
        if N:
            if config.L <= 12:
                return round((config.L) * N, dec)
            else:
                n = ceil(config.L/12)
                nd = 56 if D<20 else 70
                return round(((config.L) + n * D * nd / 1000) * N, dec)
        else:
            if config.L <= 12:
                return round((config.L), dec)
            else:
                n = ceil(config.L/12)
                nd = 56 if D<20 else 70
                return round(((config.L) + n * D * nd / 1000), dec)
            

# I should check the total weigth
