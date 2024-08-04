import pandas as pd
import numpy as np
from bridge_autocad_modular.Tables import Tables
from math import ceil, pi, cos

class Calculate:
    def __init__(self, file):
        self._config(file)
        self._store_tables()
        self.data = {}
        self.apply_directions()
        self.apply_bottom()
        self.apply_table1(self.find_in_table1(Hs=self.Hs, H=self.H))
        self.apply_table2(self.find_in_table2(Hs=self.Hs))
        self.apply_table3(self.find_in_table3(h_min=self.H_min))


        for k, v in self.data.items():
            self.data[k] = str(v)

    def _config(self, file):
        data = pd.read_csv(file, header=None)
        data.fillna("")
        self.n = int(data.iloc[0, 1])
        self.D = float(data.iloc[1, 1])
        self.L = float(data.iloc[2, 1])
        self.Hs = float(data.iloc[3, 1])
        self.H = float(data.iloc[4, 1])
        self.H_min = float(data.iloc[5, 1])
        self.CL = float(data.iloc[6, 1])
        self.dever_right = float(data.iloc[7, 1])
        self.dever_left = float(data.iloc[8, 1])
        self.ax_nature = float(data.iloc[9, 1])
        self.z_nature = float(data.iloc[10, 1])
        self.z_toli = float(data.iloc[11, 1])
        self.z_shirvani = int(data.iloc[12, 1])
        self.ret = float(data.iloc[13, 1])
        self.ball_degre = float(data.iloc[14, 1])
        self.A = float(data.iloc[15, 1])
        self.B = float(data.iloc[16, 1])


        self.city_top = data.iloc[17, 1]
        self.city_down = data.iloc[18, 1]

        if data.iloc[19, 1] == True or data.iloc[19, 1] == "True":
            self.left = "UP"
            self.right = "DOWN"
        elif data.iloc[19, 1] == False or data.iloc[19, 1] == "False":
            self.left = "DOWN"
            self.right = "UP"
        else:
            self.left = ""
            self.right = ""

        self.explanation1 = data.iloc[20, 1]
        self.explanation2 = data.iloc[21, 1]
        self.explanation3 = data.iloc[22, 1]
        self.mozo_nagshe1 = data.iloc[23, 1]
        self.mozo_nagshe2 = data.iloc[24, 1]
        self.mozo_nagshe3 = data.iloc[25, 1]
        self.number_nagshe = data.iloc[26, 1]
        self.karfarma = data.iloc[27, 1]
        self.mohandes_moshaver = data.iloc[28, 1]
        self.peymankar = data.iloc[29, 1]
        self.onvan_project = data.iloc[30, 1]
        self.date_eblagh = data.iloc[31, 1]
        self.abro_dahane = data.iloc[32, 1]
        self.mahal_abro = data.iloc[33, 1]
        self.hadaksar_ertefa_abro = data.iloc[34, 1]
        self.zavie_torb = data.iloc[35, 1]
        self.tozihat1 = data.iloc[35, 1]
        self.tozihat2 = data.iloc[36, 1]
        self.tozihat3 = data.iloc[37, 1]
        self.tozihat4 = data.iloc[38, 1]

        print("[INFO] All input data were read successfuly.")

    def _store_tables(self):
        table = Tables()
        if self.n == 1:
            self.t1 = table.one_table
            self.t2 = table.full_table
            self.t3 = table.bal_table

    def find_in_table1(self, Hs:float, H:float) -> pd.Series:
        t1 = self.t1
        mask_temp_1 = t1["n"] == self.n
        mask_temp_2 = t1["D"] == self.D
        mask_temp_3 = t1["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t1[mask]
        choice = choice[choice["H"] > H].min(axis=0)
        if np.isnan(choice[0]):
            print(f"[Wrong] There is no such {self.n} and {self.D} and {H} and {Hs} in the table.\nYou can change the Hs or you can change the D and try again.")
            return "DONE_E"
        else:
            print(f"[INFO] Successfuly find parameters in the table 1.")
            return choice
        
    def find_in_table2(self, Hs:float) -> pd.Series:
        t2 = self.t2
        mask_temp_1 = t2["n"] == self.n
        mask_temp_2 = t2["D"] == self.D
        mask_temp_3 = t2["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t2[mask]
        print(f"[INFO] Successfuly find parameters in the table 2.")
        return choice.iloc[0, :]
    
    def find_in_table3(self, h_min:float) -> list[pd.Series, pd.Series]:
        t3 = self.t3
        choice = []
        h_max_l = self.data["i-100"] + 0.3 + self.data["i-t"] - self.data["i-101"]
        h_max_r = self.data["i-103"] + 0.3 + self.data["i-t"] - self.data["i-104"]
        for H in [h_min, h_max_l, h_max_r]:
            if not t3[t3["H"]==H].empty:
                choice.append(pd.Series(t3[t3["H"] == H].iloc[0, :]))
            else:
                if H > 7 or H < 1:
                    print(f"[ERROR] Max H is incorrect. H = {H}. should be between 1 and 7.")
                    return None
                lower = t3[t3["H"] < H].iloc[-1]
                upper = t3[t3["H"] > H].iloc[0]
                lower_H = lower['H']
                upper_H = upper['H']
                weight = (H - lower_H) / (upper_H - lower_H)
                interpolated_row = lower + weight * (upper - lower)
                choice.append(interpolated_row)
        print(f"[INFO] Successfuly find parameters in the table 3.")
        return choice
    
    def apply_directions(self):
        self.data["i-092"] = self.left
        self.data["i-093"] = self.city_top
        self.data["i-094"] = self.city_down
        self.data["i-095"] = self.right
        print(f"[INFO] Successfuly applied parameters in the for directions.")

    def apply_bottom(self):
        self.data["i-173"] = self.explanation1
        self.data["i-174"] = self.explanation2
        self.data["i-175"] = self.explanation3
        self.data["i-169"] = self.mozo_nagshe1
        self.data["i-170"] = self.mozo_nagshe2
        self.data["i-171"] = self.mozo_nagshe3
        self.data["i-172"] = self.number_nagshe
        self.data["i-167"] = self.karfarma
        self.data["i-168"] = self.mohandes_moshaver
        self.data["i-165"] = self.peymankar
        self.data["i-166"] = self.onvan_project
        self.data["i_163"] = self.number_nagshe
        self.data["i-164"] = self.date_eblagh
        self.data["i-161"] = self.abro_dahane
        self.data["i-162"] = self.mahal_abro
        self.data["i-176"] = self.hadaksar_ertefa_abro
        self.data["i-177"] = self.zavie_torb
        self.data["i-178"] = self.tozihat1
        self.data["i-179"] = self.tozihat2
        self.data["i-180"] = self.tozihat3
        self.data["i-181"] = self.tozihat4
        print(f"[INFO] Successfuly applied information in the for footer.")


    def apply_table1(self, d: pd.Series):
        self.data["i-097"] = round(self.CL, 2)
        self.data["i-098"] = round(self.dever_left*100, 0)
        self.data["i-099"] = round(self.dever_right*100, 0)
        self.data["i-182"] = round(self.z_shirvani*100, 0)
        self.data["i-A"] = self.A
        self.data["i-B"] = self.B
        self.data["i-L"] = self.L
        self.data["i-100"] = round(self.data["i-097"] + self.data["i-098"] * self.data["i-A"] - self.Hs - d["t"] - 0.3, 2)
        self.data["i-103"] = round(self.data["i-097"] + self.data["i-099"] * self.data["i-B"] - self.Hs - d["t"] - 0.3, 2)
        if self.data["i-092"] == "UP":
            self.data["i-101"] = round(self.ax_nature + self.z_nature * self.data["i-A"] - self.ret, 2)
            self.data["i-104"] = round(self.ax_nature - self.z_nature * self.data["i-A"] - self.ret, 2)
        elif self.data["i-092"] == "DOWN":
            self.data["i-101"] = round(self.ax_nature - self.z_nature * self.data["i-A"] - self.ret, 2)
            self.data["i-104"] = round(self.ax_nature + self.z_nature * self.data["i-A"] - self.ret, 2)
        else:
            print(f"[INFO] Not implemeted down and up(i-092 and i-095)")
        self.data["i-102"] = round(self.data["i-101"] - d["m"], 2)
        self.data["i-105"] = round(self.data["i-104"] - d["m"], 2)

        self.data["i-096"] = round(self.z_toli*100, 0)
        self.data["i-c2"] = d["c2"]
        self.data["i-c1"] = d["c1"]
        self.data["i-Hs"] = self.Hs
        self.data["i-j"] = d["j*"]
        self.data["i-t"] = d["t"]
        self.data["i-b2"] = d["b2"]
        self.data["i-H"] = "?????????????"
        self.data["i-a1"] = d["a1"]
        self.data["i-b2"] = d["b2"]
        self.data["i-a2"] = d["a2"]
        self.data["i-m"] = d["m"]
        self.data["i-f"] = d["f"]
        self.data["i-D"] = self.D
        print(f"[INFO] Successfuly applied parameters from the table 1.")


    def apply_table2(self, d:pd.Series):
        self.data["i-001"] = d["p1_diameter(mm)"]
        self.data["i-002"] = self.count_in_pos(1, d["p1_n"])
        self.data["i-003"] = d["p1_sh_i1"]
        self.data["i-004"] = d["p1_sh_i2"]
        self.data["i-005"] = d["p1_sh_i3"]
        self.data["i-006"] = d["p1_sh_i4"]
        self.data["i-007"] = d["p1_sh_i1"]
        self.data["i-008"] = round(float(d["p1_L(m)"]), 1)
        self.data["i-009"] = round(float(d["p1_L(m)"])*float(self.count_in_pos(1, d["p1_n"], cal=True)), 2)
        self.data["i-010"] = self.weight_in_pos(d["p1_diameter(mm)"], dec=3)
        self.data["i-011"] = self.weight_in_pos(d["p1_diameter(mm)"], self.data["i-009"], 2) 
        self.data["i-012"] = d["p2_diameter(mm)"]
        self.data["i-013"] = self.count_in_pos(2, d["p2_n"])
        self.data["i-014"] = d["p2_sh_i1"]
        self.data["i-015"] = d["p2_sh_i2"]
        self.data["i-016"] = d["p2_sh_i3"]
        self.data["i-017"] = d["p2_sh_i4"]
        self.data["i-018"] = d["p2_sh_i1"]
        self.data["i-019"] = round(float(d["p2_L(m)"]), 1)
        self.data["i-020"] = round(float(d["p1_L(m)"])*float(self.count_in_pos(1, d["p2_n"], cal=True)), 2)
        self.data["i-021"] = self.weight_in_pos(d["p2_diameter(mm)"], dec=3)
        self.data["i-022"] = self.weight_in_pos(d["p2_diameter(mm)"], self.data["i-020"], 2)
        self.data["i-023"] = d["p3_diameter(mm)"]
        self.data["i-024"] = self.count_in_pos(3, d["p3_n"])
        self.data["i-025"] = d["p3_sh_i1"]
        self.data["i-026"] = self.lengh_in_pos(d["p3_diameter(mm)"])
        self.data["i-027"] = self.lengh_in_pos(d["p3_diameter(mm)"], float(self.count_in_pos(3, d["p3_n"], cal=True)), 2)
        self.data["i-028"] = self.weight_in_pos(d["p3_diameter(mm)"], dec=3)
        self.data["i-029"] = self.weight_in_pos(d["p3_diameter(mm)"], self.data["i-027"], 2)
        self.data["i-030"] = d["p4_diameter(mm)"]
        self.data["i-031"] = self.count_in_pos(4, d["p4_n"])
        self.data["i-032"] = d["p4_sh_i1"]
        self.data["i-033"] = d["p4_sh_i2"]
        self.data["i-034"] = d["p4_sh_i1"]
        self.data["i-035"] = round(float(d["p4_L(m)"]), 1)
        self.data["i-036"] = round(float(d["p4_L(m)"])*float(self.count_in_pos(4, d["p4_n"], cal=True)), 2)
        self.data["i-037"] = self.weight_in_pos(d["p4_diameter(mm)"], dec=3)
        self.data["i-038"] = self.weight_in_pos(d["p4_diameter(mm)"], self.data["i-036"], 2)
        self.data["i-039"] = d["p5_diameter(mm)"]
        self.data["i-040"] = self.count_in_pos(5, d["p5_n"])
        self.data["i-041"] = d["p5_sh_i1"]
        self.data["i-042"] = self.lengh_in_pos(d["p5_diameter(mm)"])
        self.data["i-043"] = self.lengh_in_pos(d["p5_diameter(mm)"], float(self.count_in_pos(5, d["p5_n"], cal=True)), 2)
        self.data["i-044"] = self.weight_in_pos(d["p5_diameter(mm)"], dec=3)
        self.data["i-045"] = self.weight_in_pos(d["p5_diameter(mm)"], self.data["i-043"], 2)
        self.data["i-046"] = d["p6_diameter(mm)"]
        self.data["i-047"] = self.count_in_pos(6, d["p6_n"])
        self.data["i-048"] = d["p6_sh_i1"]
        self.data["i-049"] = self.lengh_in_pos(d["p6_diameter(mm)"])
        self.data["i-050"] = self.lengh_in_pos(d["p6_diameter(mm)"], float(self.count_in_pos(6, d["p6_n"], cal=True)), 2)
        self.data["i-051"] = self.weight_in_pos(d["p6_diameter(mm)"], dec=3)
        self.data["i-052"] = self.weight_in_pos(d["p6_diameter(mm)"], self.data["i-050"], 2)
        self.data["i-053"] = d["p7_diameter(mm)"]
        self.data["i-054"] = self.count_in_pos(7, d["p7_n"])
        self.data["i-055"] = d["p7_sh_i1"]
        self.data["i-056"] = d["p7_sh_i2"]
        self.data["i-057"] = d["p7_sh_i3"]
        self.data["i-058"] = d["p7_sh_i4"]
        self.data["i-059"] = round(float(d["p7_L(m)"]))
        self.data["i-060"] = round(float(d["p7_L(m)"])*float(self.count_in_pos(7, d["p7_n"], cal=True)), 2)
        self.data["i-061"] = self.weight_in_pos(d["p7_diameter(mm)"], dec=3)
        self.data["i-062"] = self.weight_in_pos(d["p7_diameter(mm)"], self.data["i-060"], 2)
        self.data["i-063"] = d["p8_diameter(mm)"]
        self.data["i-064"] = self.count_in_pos(8, d["p8_n"])
        self.data["i-065"] = d["p8_sh_i1"]
        self.data["i-066"] = round(float(d["p8_L(m)"]))
        self.data["i-067"] = round(float(d["p8_L(m)"])*float(self.count_in_pos(8, d["p8_n"], cal=True)), 2)
        self.data["i-068"] = self.weight_in_pos(d["p8_diameter(mm)"], dec=3)
        self.data["i-069"] = self.weight_in_pos(d["p8_diameter(mm)"], self.data["i-067"], 2)
        self.data["i-070"] = d["p9_diameter(mm)"]
        self.data["i-071"] = self.count_in_pos(9, d["p9_n"])
        self.data["i-072"] = d["p9_sh_i1"]
        self.data["i-073"] = d["p9_sh_i2"]
        self.data["i-074"] = d["p9_sh_i3"]
        self.data["i-075"] = d["p9_sh_i4"]
        self.data["i-076"] = d["p9_sh_i5"]
        self.data["i-077"] = round(float(d["p9_L(m)"]))
        self.data["i-078"] = round(float(d["p9_L(m)"])*float(self.count_in_pos(9, d["p9_n"], cal=True)), 2)
        self.data["i-079"] = self.weight_in_pos(d["p9_diameter(mm)"], dec=3)
        self.data["i-080"] = self.weight_in_pos(d["p9_diameter(mm)"], self.data["i-078"], 2)
        self.data["i-081"] = d["p0_diameter(mm)"]
        self.data["i-082"] = self.count_in_pos(10, d["p0_n"])
        if self.data["i-082"] != "-":
            self.data["i-083"] = d["p0_sh_i1"] + " / " + d["p0_sh_i2"]
            self.data["i-084"] = d["p0_sh_i3"]
            self.data["i-085"] = round(float(d["p1_L(m)"]))
            self.data["i-086"] = round(float(d["p1_L(m)"])*float(self.count_in_pos(10, d["p0_n"], cal=True)), 2)
            self.data["i-087"] = self.weight_in_pos(d["p0_diameter(mm)"], dec=3)
            self.data["i-088"] = self.weight_in_pos(d["p0_diameter(mm)"], self.data["i-086"], 1) if self.weight_in_pos(d["p0_diameter(mm)"], dec=1) != "-" else "-"
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
        self.data["i-089"] = round(sum([float(i) for i in c_temp[0]]) / self.L, 1)
        self.data["i-090"] = round(sum([float(i) for i in c_temp[1]]), 1)
        self.data["i-091"] = round(sum([float(i) for i in c_temp[2]]), 1)
        print(f"[INFO] Successfuly applied parameters from the table 2.")


    def apply_table3(self, data_list:list):
        if not data_list:
            return None
        w1_distance = round(self.find_distance_for_bal(h_min=data_list[0]["H"], h_max=data_list[2]["H"], direction=self.data["i-095"]), 1)
        w2_distance = round(self.find_distance_for_bal(h_min=data_list[0]["H"], h_max=data_list[2]["H"], direction=self.data["i-095"]), 1)
        w3_distance = round(self.find_distance_for_bal(h_min=data_list[0]["H"], h_max=data_list[1]["H"], direction=self.data["i-092"]), 1)
        w4_distance = round(self.find_distance_for_bal(h_min=data_list[0]["H"], h_max=data_list[1]["H"], direction=self.data["i-092"]), 1)

        height_min = round(data_list[0]["H"], 2)
        height_pei_min = round(data_list[0]["m"], 2)
        width_pei_min = round(data_list[0]["f"], 2)
        s1_min = round(data_list[0]["f"] - data_list[0]["b"], 2)
        s2_min = round(data_list[0]["x"] + 0.35, 2)

        w1_height_max = round(data_list[2]["H"], 2)
        w2_height_max = round(data_list[2]["H"], 2)
        w3_height_max = round(data_list[1]["H"], 2)
        w4_height_max = round(data_list[1]["H"], 2)

        w1_code_first_pei = "?"
        w1_code_end_pei = "?"
        w1_code_upper_pei = "?"

        w1_height_pei_max = round(data_list[2]["m"], 2)
        w2_height_pei_max = round(data_list[2]["m"], 2)
        w3_height_pei_max = round(data_list[1]["m"], 2)
        w4_height_pei_max = round(data_list[1]["m"], 2)

        w1_width_pei_max = round(data_list[2]["f"], 2)
        w2_width_pei_max = round(data_list[2]["f"], 2)
        w3_width_pei_max = round(data_list[1]["f"], 2)
        w4_width_pei_max = round(data_list[1]["f"], 2)

        w1_s1_max = round(data_list[2]["f"] - data_list[2]["b"], 2)
        w2_s1_max = round(data_list[2]["f"] - data_list[2]["b"], 2)
        w3_s1_max = round(data_list[1]["f"] - data_list[1]["b"], 2)
        w4_s1_max = round(data_list[1]["f"] - data_list[1]["b"], 2)

        w1_s2_max = round(data_list[2]["x"] + 0.35, 2)
        w2_s2_max = round(data_list[2]["x"] + 0.35, 2)
        w3_s2_max = round(data_list[1]["x"] + 0.35, 2)
        w4_s2_max = round(data_list[1]["x"] + 0.35, 2)

        self.data["i-106"] = w1_distance
        self.data["i-120"] = w2_distance
        self.data["i-134"] = w3_distance
        self.data["i-147"] = w4_distance

        self.data["i-107"] = w1_height_max
        self.data["i-121"] = w2_height_max
        self.data["i-134"] = w3_height_max
        self.data["i-148"] = w4_height_max

        self.data["i-108"] = height_min
        self.data["i-122"] = height_min
        self.data["i-135"] = height_min
        self.data["i-149"] = height_min

        self.data["i-109"] = "--"
        self.data["i-123"] = "--"
        self.data["i-136"] = "--"
        self.data["i-150"] = "--"

        self.data["i-110"] = "--"
        self.data["i-124"] = "--"
        self.data["i-137"] = "--"
        self.data["i-151"] = "--"

        self.data["i-111"] = "--"
        self.data["i-125"] = "--"
        self.data["i-138"] = "--"
        self.data["i-152"] = "--"

        self.data["i-112"] = height_pei_min
        self.data["i-126"] = height_pei_min
        self.data["i-139"] = height_pei_min
        self.data["i-153"] = height_pei_min

        self.data["i-113"] = w1_height_pei_max
        self.data["i-127"] = w2_height_pei_max
        self.data["i-140"] = w3_height_pei_max
        self.data["i-154"] = w4_height_pei_max

        self.data["i-114"] = width_pei_min
        self.data["i-128"] = width_pei_min
        self.data["i-141"] = width_pei_min
        self.data["i-155"] = width_pei_min

        self.data["i-115"] = w1_width_pei_max
        self.data["i-129"] = w2_width_pei_max
        self.data["i-142"] = w3_width_pei_max
        self.data["i-156"] = w4_width_pei_max

        self.data["i-116"] = w1_s1_max
        self.data["i-130"] = w2_s1_max
        self.data["i-143"] = w3_s1_max
        self.data["i-157"] = w4_s1_max

        self.data["i-117"] = s1_min
        self.data["i-131"] = s1_min
        self.data["i-144"] = s1_min
        self.data["i-158"] = s1_min

        self.data["i-118"] = w1_s2_max
        self.data["i-132"] = w2_s2_max
        self.data["i-145"] = w3_s2_max
        self.data["i-159"] = w4_s2_max

        self.data["i-119"] = s2_min
        self.data["i-133"] = s2_min
        self.data["i-146"] = s2_min
        self.data["i-160"] = s2_min
        print(f"[INFO] Successfuly applied parameters from the table 3.")


    def find_distance_for_bal(self, h_min, h_max, direction):
        def formula(hmax, hmin):
            return (hmax-hmin)/cos(self.ball_degre) * self.z_shirvani
        
        h_min_temp = h_min
        d1, d2 = 0, 1
        if direction == "UP":
            while abs(d2-d1) > 0.2:
                d1 = formula(hmax=h_max, hmin=h_min_temp)
                h_min_temp = 1 + d1*self.z_nature
                d2 = formula(hmax=h_max, hmin=h_min_temp)
        elif direction == "DOWN":
            while abs(d2-d1) > 0.2:
                d1 = formula(hmax=h_max, hmin=h_min_temp)
                h_min_temp = 1 - d1*self.z_nature
                d2 = formula(hmax=h_max, hmin=h_min_temp)
        print(f"[INFO] Find the distance in {direction} for min height of {h_min} and max height of {h_max}.")
        return d2

    def count_in_pos(self, p:int, count:str, cal=False):
        if count == "-":
            return "-"
        else:
            try:
                count_p1, count_p2 = count.split("*")
            except:
                count_p1, count_p2 = count, None
            if p in [1, 2, 4, 7, 10]:
                res = self.L * float(count_p1)
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
        
    def weight_in_pos(self, D:float, L:float=None, dec:int=1) -> float:
        if D == "-":
            return "-"
        else:
            if L:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res*L, dec)
            else:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res, dec)
    
    def lengh_in_pos(self, D:float, N:float=None, dec=1) -> float:
        if N:
            if self.L <= 12:
                return round((self.L) * N, dec)
            else:
                n = ceil(self.L/12)
                nd = 56 if D<20 else 70
                return round(((self.L) + n * D * nd / 1000) * N, dec)
        else:
            if self.L <= 12:
                return round((self.L), dec)
            else:
                n = ceil(self.L/12)
                nd = 56 if D<20 else 70
                return round(((self.L) + n * D * nd / 1000), dec)
            
