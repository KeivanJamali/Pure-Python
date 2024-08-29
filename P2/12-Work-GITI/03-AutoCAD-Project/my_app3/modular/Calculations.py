import pandas as pd
import numpy as np
from modular.Tables import Tables
from math import ceil, pi, cos, radians

class Calculate:
    def __init__(self, file, progress_callback=None):
        self.progress_callback=progress_callback
        self.massage1, self.massage2, self.massage3 = None, None, None
        self.massage = None
        self.data = {}
        input_wrong = self._config(file)
        if not input_wrong:
            if self.progress_callback:
                self.progress_callback(40)
            if self.n == 1:
                self._step1()
            elif self.n == 2:
                self._step2()
            elif self.n == 3:
                self._step3()
            elif self.n == 4:
                self._step4()
            elif self.n == 5:
                self._step5()
            elif self.n == 6:
                self._step6()
            elif self.n == 7:
                self._step7()
            elif self.n == 8:
                self._step8()
        mss = []
        if input_wrong:
            mss.append(str(input_wrong))
        if self.massage1:
            mss.append(str(self.massage1))
        if self.massage2:
            mss.append(str(self.massage2))
        if self.massage3:
            mss.append(str(self.massage3))
        self.massage = " / ".join(mss)

    def _step1(self):
        """In this functions we prepare the result for n=1 culvert.
        """
        self._store_tables()
        if self.progress_callback:
            self.progress_callback(50)
        self.apply_directions()
        # self.apply_bottom()
        self.massage1 = self.apply_table1(self.find_in_table1(Hs=self.Hs))
        if not self.massage1:
            self.massage2 = self.apply_table2(self.find_in_table2(Hs=self.Hs))
            self.massage3 = self.apply_table3(self.find_in_table3(h_min=self.H_min))
        if self.progress_callback:
            self.progress_callback(65)

        for k, v in self.data.items():
            self.data[k] = str(v)

    def _step2(self):
        """In this function we prepare the result for n=1 culvert angular.
        """
        pass

    def _step3(self):
        """In this function we prepare the result for n>1 culvert.
        """
        pass

    def _step4(self):
        """In this function we prepare the result for n>1 culvert angular.
        """
        pass

    def _step5(self):
        """In this function we prepare the result for n=1 underground culvert.
        """
        pass

    def _step6(self):
        """In this function we prepare the result for n=1 underground culvert angular.
        """
        pass

    def _step7(self):
        """In this function we prepare the result for n>1 underground culvert.
        """
        pass

    def _step8(self):
        """In this function we prepare the result for n>1 underground culvert angular.
        """
        pass
        
    def _config(self, file:str) -> bool:
        """We get all the inputs and parametrize them by reading the csv file.

        Args:
            file (str): The input csv file.

        Returns:
            bool: If data is correct it returns False, unless it will returns str.
        """
        data = self._read_data(file)
        if type(data) == str:
            return data
        else:
            done = self._put_initial_data(data)
            return done
    
    def _read_data(self, file:str) -> pd.DataFrame:
        """Thsi function will store the data in parameter as pd.DataFrame.

        Args:
            file (str): The input csv file name.

        Returns:
            pd.DataFrame: All the data in table.
        """
        try:
            data = pd.read_csv(file, header=None)
        except:
            print("[ERROR] Not enough input. Try again. ---Calculations - line 124---")
            return "[ERROR] Not enough input. Try again. ---Calculations - line 125---"
        data.fillna("")
        return data

    def _put_initial_data(self, data: pd.DataFrame) -> bool:
        """This function will put all the data in parameters n, D, L, Hs, H, ... .

        Args:
            data (pd.DataFrame): The input csv file that is now represented as DataFrame.

        Returns:
            bool: If everything is correct it will return False. If some errors happens it will return Some Text(True).
        """
        try:
            self.n = int(data.iloc[0, 1])
            self.D = float(data.iloc[1, 1])
            self.L = float(data.iloc[2, 1])
            self.Hs = float(data.iloc[3, 1])
            self.H = 0
            self.H_min = float(data.iloc[4, 1])
            self.CL = float(data.iloc[5, 1])
            self.ax_natural = float(data.iloc[6, 1])
            self.dever_right = float(data.iloc[7, 1])
            self.dever_left = float(data.iloc[8, 1])
            self.z_natural = float(data.iloc[9, 1])
            self.z_toli = float(data.iloc[10, 1])
            self.z_shirvani = int(data.iloc[11, 1])
            self.ret = float(data.iloc[12, 1])
            self.ball_degre = float(data.iloc[13, 1])
            self.A = float(data.iloc[14, 1])
            self.B = float(data.iloc[15, 1])
            if data.iloc[16, 1] in [True, "TRUE", "true", "True"]:
                self.left = "UP"
                self.right = "DOWN"
            elif data.iloc[16, 1] in [False, "FALSE", "false", "False"]:
                self.left = "DOWN"
                self.right = "UP"
            else:
                self.left = ""
                self.right = ""

            # self.city_top = data.iloc[17, 1]
            # self.city_down = data.iloc[18, 1]
            # self.explanation1 = data.iloc[19, 1]
            # self.explanation2 = data.iloc[20, 1]
            # self.explanation3 = data.iloc[21, 1]
            # self.mozo_nagshe1 = data.iloc[22, 1]
            # self.mozo_nagshe2 = data.iloc[23, 1]
            # self.mozo_nagshe3 = data.iloc[24, 1]
            # self.number_nagshe = data.iloc[25, 1]
            # self.karfarma = data.iloc[26, 1]
            # self.mohandes_moshaver = data.iloc[27, 1]
            # self.peymankar = data.iloc[28, 1]
            # self.onvan_project = data.iloc[29, 1]
            # self.date_eblagh = data.iloc[30, 1]
            # self.abro_dahane = data.iloc[31, 1]
            # self.mahal_abro = data.iloc[32, 1]
            # self.hadaksar_ertefa_abro = data.iloc[33, 1]
            # self.zavie_torb = data.iloc[34, 1]
        except:
            print("[ERROR] Not enough input2. Try again. ---Calculations - line 185---")
            return "[ERROR] Not enough input2. Try again. ---Calculations - line 186---"

        print("[INFO] All input data were read successfuly. ---Calculations - line 188---")
        return False

    def _store_tables(self):
        """This function will read all the tables and store them for later usages.
        """
        table = Tables()
        if self.n == 1:
            self.t1 = table.one_table
            self.t2 = table.full_table
            self.t3 = table.bal_table

    def find_in_table1(self, Hs:float) -> pd.Series:
        """This function will check the table to find the correct row of it and store and return the row to us.
        This table contains data of a1, a2, b1, b2, c1, c2, f, m, t, phi_b, j*.
        We check Hs, n and D for it.

        Args:
            Hs (float): HS parameter.

        Returns:
            pd.Series: The finded result as a series.
        """
        t1 = self.t1
        mask_temp_1 = t1["n"] == self.n
        mask_temp_2 = t1["D"] == self.D
        mask_temp_3 = t1["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t1[mask]
        choice = choice[choice["H"] > self.H].min(axis=0)
        if np.isnan(choice[0]):
            print(f"[Wrong] H did not stisfied in the table.\n[INFO] You can change the Hs or you can change the D and try again. ---Calculations - line 220---")
            return str(f"[Wrong] H did not stisfied in the table.\n[INFO] You can change the Hs or you can change the D and try again. ---Calculations - line 221---")
        else:
            print(f"[INFO] Successfuly find parameters in the table 1. ---Calculations - line 223---")
            return choice
        
    def find_in_table2(self, Hs:float) -> pd.Series:
        """This function will check the table to find the correct row of it and store and return the row to us.
        This table contains all the data about diffrent posisions. The largest table:)
        We give it n and D and Hs.
        
        Args:
            Hs (float): Hs Parameter.

        Returns:
            pd.Series: The finded result as a series.
        """
        t2 = self.t2
        mask_temp_1 = t2["n"] == self.n
        mask_temp_2 = t2["D"] == self.D
        mask_temp_3 = t2["Hs"].apply(lambda x: Hs>float(x[1:4]) and Hs<float(x[7:11]))
        mask = mask_temp_1.astype(int) + mask_temp_2.astype(int) + mask_temp_3.astype(int)
        mask = mask==3
        choice = t2[mask]
        print(f"[INFO] Successfuly find parameters in the table 2. ---Calculations - line 244---")
        return choice.iloc[0, :]
    
    def find_in_table3(self, h_min:float) -> list[pd.Series, pd.Series, pd.Series]:
        """This function will check the table to find the correct row of it and store and return the row to us.
        This table contains b, f, m, x
        We give H as input.

        Args:
            h_min (float): Minimum h that we want.

        Returns:
            list[pd.Series, pd.Series, pd.Series]: All 3 possiable series for the answer. [H_min, H_max_left, H_max_right]
        """
        t3 = self.t3
        choice = []
        h_max_l = self.data["i-100"] + 0.3 + self.data["i-t"] - self.data["i-101"]
        h_max_r = self.data["i-103"] + 0.3 + self.data["i-t"] - self.data["i-104"]
        for H in [h_min, h_max_l, h_max_r]:
            if not t3[t3["H"]==H].empty:
                choice.append(pd.Series(t3[t3["H"] == H].iloc[0, :]))
            else:
                if H > 7 or H < 1:
                    print(f"[ERROR] Max H is incorrect. H = {H}. should be between 1 and 7. ---Calculations - line 267---")
                    return f"[ERROR] Max H is incorrect. H = {H}. should be between 1 and 7. ---Calculations - line 268---"
                lower = t3[t3["H"] < H].iloc[-1]
                upper = t3[t3["H"] > H].iloc[0]
                lower_H = lower['H']
                upper_H = upper['H']
                weight = (H - lower_H) / (upper_H - lower_H)
                interpolated_row = lower + weight * (upper - lower)
                choice.append(interpolated_row)
        print(f"[INFO] Successfuly find parameters in the table 3. ---Calculatinos - line 276---")
        return choice
    
    def apply_directions(self):
        """This functino will put the name of directions and cities.
        """
        self.data["i-092"] = self.left
        self.data["i-093"] = self.city_top
        self.data["i-094"] = self.city_down
        self.data["i-095"] = self.right
        print(f"[INFO] Successfuly applied parameters in the for directions. ---Calculations - line 286---")

    def apply_bottom(self):
        """Filling the bottom part of the page.
        """
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
        print(f"[INFO] Successfuly applied information in the for footer. ---Calculations - line 308---")


    def apply_table1(self, d: pd.Series) -> None:
        """This functions will apply all the information from table 1 to parameters with n=1.

        Args:
            d (pd.Series): The selected row in the table1.

        Returns:
            None
        """
        if type(d) == str:
            return d
        self.data["i-097"] = round(self.CL, 2)
        self.data["i-098"] = int(round(self.dever_left*100, 0))
        self.data["i-099"] = int(round(self.dever_right*100, 0))
        self.data["i-182"] = int(round(self.z_shirvani*100, 0))
        self.data["i-A"] = self.A
        self.data["i-B"] = self.B
        self.data["i-L"] = self.L
        self.data["i-100"] = round(self.data["i-097"] + (self.data["i-098"]/100) * self.data["i-A"] - self.Hs - d["t"] - 0.3, 2)
        self.data["i-103"] = round(self.data["i-097"] + (self.data["i-099"]/100) * self.data["i-B"] - self.Hs - d["t"] - 0.3, 2)
        if self.data["i-092"] == "UP":
            self.data["i-101"] = round(self.ax_natural + self.z_natural * self.data["i-A"] - self.ret, 2)
            self.data["i-104"] = round(self.ax_natural - self.z_natural * self.data["i-B"] - self.ret, 2)
        elif self.data["i-092"] == "DOWN":
            self.data["i-101"] = round(self.ax_natural - self.z_natural * self.data["i-A"] - self.ret, 2)
            self.data["i-104"] = round(self.ax_natural + self.z_natural * self.data["i-B"] - self.ret, 2)
        else:
            print(f"[INFO] Not implemeted down and up(i-092 and i-095). ---Calculation - line 216---")
        self.data["i-102"] = round(self.data["i-101"] - d["m"], 2)
        self.data["i-105"] = round(self.data["i-104"] - d["m"], 2)

        self.H_1 = self.data["i-100"] - self.data["i-101"] + 0.3
        self.H_2 = self.data["i-103"] - self.data["i-104"] + 0.3
        self.H = round((self.H_1+self.H_2)/2, 2)
        print(f"[INFO] We found the H={self.H}. Now let's check with {d["H"]}. --- Calculation - line 223---")
        if self.H >= d["H"]:
            print(f"[Wrong]...")
            self.H = d["H"]
            return self.apply_table1(self.find_in_table1(Hs=self.Hs))
        print(f"[INFO] H={self.H} successful. ---Calculation - line 228---")
        self.data["i-H"] = self.H
        self.data["i-096"] = int(round(self.z_toli*100, 0))
        self.data["i-c2"] = d["c2"]
        self.data["i-c1"] = d["c1"]
        self.data["i-Hs"] = self.Hs
        self.data["i-j"] = d["j*"]
        self.data["i-t"] = d["t"]
        self.data["i-b2"] = d["b2"]
        self.data["i-a1"] = d["a1"]
        self.data["i-b2"] = d["b2"]
        self.data["i-a2"] = d["a2"]
        self.data["i-m"] = d["m"]
        self.data["i-f"] = d["f"]
        self.data["i-D"] = self.D
        print(f"[INFO] Successfuly applied parameters from the table 1. ---Calcuaion - line 243---")

    def apply_table2(self, d:pd.Series) -> None:
        """This functions will apply all the information from table 2 to parameters with n=1.

        Args:
            d (pd.Series): The selected row in the table2.

        Returns:
            None
        """
        self.data["i-001"] = d["p1_diameter(mm)"]
        self.data["i-002"] = self.count_in_pos(1, d["p1_n"])
        self.data["i-003"] = d["p1_sh_i1"]
        self.data["i-004"] = d["p1_sh_i2"]
        self.data["i-005"] = d["p1_sh_i3"]
        self.data["i-006"] = d["p1_sh_i4"]
        self.data["i-007"] = d["p1_sh_i1"]
        self.data["i-008"] = self.lengh_in_pos(p=1, L=d["p1_L(m)"], D=d["p1_diameter(mm)"])
        self.data["i-009"] = self.lengh_in_pos(p=1, L=d["p1_L(m)"], N=self.count_in_pos(1, d["p1_n"], cal=True), D=d["p1_diameter(mm)"], dec=2)
        self.data["i-010"] = self.weight_in_pos(d["p1_diameter(mm)"], dec=3)
        self.data["i-011"] = self.weight_in_pos(d["p1_diameter(mm)"], self.data["i-009"], 2) 
        self.data["i-012"] = d["p2_diameter(mm)"]
        self.data["i-013"] = self.count_in_pos(2, d["p2_n"])
        self.data["i-014"] = d["p2_sh_i1"]
        self.data["i-015"] = d["p2_sh_i2"]
        self.data["i-016"] = d["p2_sh_i3"]
        self.data["i-017"] = d["p2_sh_i4"]
        self.data["i-018"] = d["p2_sh_i1"]
        self.data["i-019"] = self.lengh_in_pos(p=2, L=d["p2_L(m)"], D=d["p2_diameter(mm)"])
        self.data["i-020"] = self.lengh_in_pos(p=2, L=d["p2_L(m)"], N=self.count_in_pos(2, d["p2_n"], cal=True), D=d["p2_diameter(mm)"], dec=2)
        self.data["i-021"] = self.weight_in_pos(d["p2_diameter(mm)"], dec=3)
        self.data["i-022"] = self.weight_in_pos(d["p2_diameter(mm)"], self.data["i-020"], 2)
        self.data["i-023"] = d["p3_diameter(mm)"]
        self.data["i-024"] = self.count_in_pos(3, d["p3_n"])
        self.data["i-025"] = d["p3_sh_i1"]
        self.data["i-026"] = self.lengh_in_pos(p=3, L=d["p3_L(m)"], D=d["p3_diameter(mm)"])
        self.data["i-027"] = self.lengh_in_pos(p=3, L=d["p3_L(m)"], N=self.count_in_pos(3, d["p3_n"], cal=True), D=d["p3_diameter(mm)"], dec=2)
        self.data["i-028"] = self.weight_in_pos(d["p3_diameter(mm)"], dec=3)
        self.data["i-029"] = self.weight_in_pos(d["p3_diameter(mm)"], self.data["i-027"], 2)
        self.data["i-030"] = d["p4_diameter(mm)"]
        self.data["i-031"] = self.count_in_pos(4, d["p4_n"])
        self.data["i-032"] = d["p4_sh_i1"]
        self.data["i-033"] = d["p4_sh_i2"]
        self.data["i-034"] = d["p4_sh_i1"]
        self.data["i-035"] = self.lengh_in_pos(p=4, L=d["p4_L(m)"], D=d["p4_diameter(mm)"])
        self.data["i-036"] = self.lengh_in_pos(p=4, L=d["p4_L(m)"], N=self.count_in_pos(4, d["p4_n"], cal=True), D=d["p4_diameter(mm)"], dec=2)
        self.data["i-037"] = self.weight_in_pos(d["p4_diameter(mm)"], dec=3)
        self.data["i-038"] = self.weight_in_pos(d["p4_diameter(mm)"], self.data["i-036"], 2)
        self.data["i-039"] = d["p5_diameter(mm)"]
        self.data["i-040"] = self.count_in_pos(5, d["p5_n"])
        self.data["i-041"] = d["p5_sh_i1"]
        self.data["i-042"] = self.lengh_in_pos(p=5, L=d["p5_L(m)"], D=d["p5_diameter(mm)"])
        self.data["i-043"] = self.lengh_in_pos(p=5, L=d["p5_L(m)"], N=self.count_in_pos(5, d["p5_n"], cal=True), D=d["p5_diameter(mm)"], dec=2)
        self.data["i-044"] = self.weight_in_pos(d["p5_diameter(mm)"], dec=3)
        self.data["i-045"] = self.weight_in_pos(d["p5_diameter(mm)"], self.data["i-043"], 2)
        self.data["i-046"] = d["p6_diameter(mm)"]
        self.data["i-047"] = self.count_in_pos(6, d["p6_n"])
        self.data["i-048"] = d["p6_sh_i1"]
        self.data["i-049"] = self.lengh_in_pos(p=6, L=d["p6_L(m)"], D=d["p6_diameter(mm)"])
        self.data["i-050"] = self.lengh_in_pos(p=6, L=d["p6_L(m)"], N=self.count_in_pos(6, d["p6_n"], cal=True), D=d["p6_diameter(mm)"], dec=2)
        self.data["i-051"] = self.weight_in_pos(d["p6_diameter(mm)"], dec=3)
        self.data["i-052"] = self.weight_in_pos(d["p6_diameter(mm)"], self.data["i-050"], 2)
        self.data["i-053"] = d["p7_diameter(mm)"]
        self.data["i-054"] = self.count_in_pos(7, d["p7_n"])
        self.data["i-055"] = d["p7_sh_i1"]
        self.data["i-056"] = d["p7_sh_i2"]
        self.data["i-057"] = d["p7_sh_i3"]
        self.data["i-058"] = d["p7_sh_i4"]
        self.data["i-059"] = self.lengh_in_pos(p=7, L=d["p7_L(m)"], D=d["p7_diameter(mm)"])
        self.data["i-060"] = self.lengh_in_pos(p=7, L=d["p7_L(m)"], N=self.count_in_pos(7, d["p7_n"], cal=True), D=d["p7_diameter(mm)"], dec=2)
        self.data["i-061"] = self.weight_in_pos(d["p7_diameter(mm)"], dec=3)
        self.data["i-062"] = self.weight_in_pos(d["p7_diameter(mm)"], self.data["i-060"], 2)
        self.data["i-063"] = d["p8_diameter(mm)"]
        self.data["i-064"] = self.count_in_pos(8, d["p8_n"])
        self.data["i-065"] = d["p8_sh_i1"]
        self.data["i-066"] = self.lengh_in_pos(p=8, L=d["p8_L(m)"], D=d["p8_diameter(mm)"])
        self.data["i-067"] = self.lengh_in_pos(p=8, L=d["p8_L(m)"], N=self.count_in_pos(8, d["p8_n"], cal=True), D=d["p8_diameter(mm)"], dec=2)
        self.data["i-068"] = self.weight_in_pos(d["p8_diameter(mm)"], dec=3)
        self.data["i-069"] = self.weight_in_pos(d["p8_diameter(mm)"], self.data["i-067"], 2)
        self.data["i-070"] = d["p9_diameter(mm)"]
        self.data["i-071"] = self.count_in_pos(9, d["p9_n"])
        self.data["i-072"] = d["p9_sh_i1"]
        self.data["i-073"] = d["p9_sh_i2"]
        self.data["i-074"] = d["p9_sh_i3"]
        self.data["i-075"] = d["p9_sh_i4"]
        self.data["i-076"] = d["p9_sh_i5"]
        self.data["i-077"] = self.lengh_in_pos(p=9, L=d["p9_L(m)"], D=d["p9_diameter(mm)"])
        self.data["i-078"] = self.lengh_in_pos(p=9, L=d["p9_L(m)"], N=self.count_in_pos(9, d["p9_n"], cal=True), D=d["p9_diameter(mm)"], dec=2)
        self.data["i-079"] = self.weight_in_pos(d["p9_diameter(mm)"], dec=3)
        self.data["i-080"] = self.weight_in_pos(d["p9_diameter(mm)"], self.data["i-078"], 2)
        self.data["i-081"] = d["p0_diameter(mm)"]
        self.data["i-082"] = self.count_in_pos(10, d["p0_n"])
        if self.data["i-082"] != "-":
            self.data["i-083"] = d["p0_sh_i1"] + " / " + d["p0_sh_i2"]
            self.data["i-084"] = d["p0_sh_i3"]
            self.data["i-085"] = self.lengh_in_pos(p=10, L=d["p0_L(m)"], D=d["p0_diameter(mm)"])
            self.data["i-086"] = self.lengh_in_pos(p=10, L=d["p0_L(m)"], N=self.count_in_pos(10, d["p0_n"], cal=True), D=d["p0_diameter(mm)"], dec=2)
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
        print(f"[INFO] Successfuly applied parameters from the table 2. ---Calculation - line 354---")


    def apply_table3(self, data_list:list) -> None:
        """This functions will apply all the information from table 3 to parameters with n=1.

        Args:
            d (pd.Series): The selected row in the table3.

        Returns:
            None
        """
        if type(data_list) == str:
            return data_list
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
        
        w1_code_first_pei = round(self.data["i-104"] - data_list[2]["m"], 2)
        w2_code_first_pei = round(self.data["i-104"] - data_list[2]["m"], 2)
        w3_code_first_pei = round(self.data["i-101"] - data_list[1]["m"], 2)
        w4_code_first_pei = round(self.data["i-101"] - data_list[1]["m"], 2)

        if self.data["i-092"] == "UP":
            w1_code_end_pei = round(self.data["i-104"] + self.z_natural * w1_distance - data_list[0]["m"], 2)
            w2_code_end_pei = round(self.data["i-104"] + self.z_natural * w2_distance - data_list[0]["m"], 2)
            w3_code_end_pei = round(self.data["i-101"] - self.z_natural * w3_distance - data_list[0]["m"], 2)
            w4_code_end_pei = round(self.data["i-101"] - self.z_natural * w4_distance - data_list[0]["m"], 2)
        elif self.data["i-092"] == "DOWN":
            w1_code_end_pei = round(self.data["i-104"] - self.z_natural * w1_distance - data_list[0]["m"], 2)
            w2_code_end_pei = round(self.data["i-104"] - self.z_natural * w2_distance - data_list[0]["m"], 2)
            w3_code_end_pei = round(self.data["i-101"] + self.z_natural * w3_distance - data_list[0]["m"], 2)
            w4_code_end_pei = round(self.data["i-101"] + self.z_natural * w4_distance - data_list[0]["m"], 2)

        code_upper_pei = "--"

        self.data["i-106"] = w1_distance
        self.data["i-120"] = w2_distance
        self.data["i-134"] = w3_distance
        self.data["i-148"] = w4_distance

        self.data["i-107"] = w1_height_max
        self.data["i-121"] = w2_height_max
        self.data["i-135"] = w3_height_max
        self.data["i-149"] = w4_height_max

        self.data["i-108"] = height_min
        self.data["i-122"] = height_min
        self.data["i-136"] = height_min
        self.data["i-150"] = height_min

        self.data["i-109"] = w1_code_first_pei
        self.data["i-123"] = w2_code_first_pei
        self.data["i-137"] = w3_code_first_pei
        self.data["i-151"] = w4_code_first_pei

        self.data["i-110"] = w1_code_end_pei
        self.data["i-124"] = w2_code_end_pei
        self.data["i-138"] = w3_code_end_pei
        self.data["i-152"] = w4_code_end_pei

        self.data["i-111"] = code_upper_pei
        self.data["i-125"] = code_upper_pei
        self.data["i-139"] = code_upper_pei
        self.data["i-153"] = code_upper_pei

        self.data["i-112"] = height_pei_min
        self.data["i-126"] = height_pei_min
        self.data["i-140"] = height_pei_min
        self.data["i-154"] = height_pei_min

        self.data["i-113"] = w1_height_pei_max
        self.data["i-127"] = w2_height_pei_max
        self.data["i-141"] = w3_height_pei_max
        self.data["i-155"] = w4_height_pei_max

        self.data["i-114"] = width_pei_min
        self.data["i-128"] = width_pei_min
        self.data["i-142"] = width_pei_min
        self.data["i-156"] = width_pei_min

        self.data["i-115"] = w1_width_pei_max
        self.data["i-129"] = w2_width_pei_max
        self.data["i-143"] = w3_width_pei_max
        self.data["i-157"] = w4_width_pei_max

        self.data["i-116"] = w1_s1_max
        self.data["i-130"] = w2_s1_max
        self.data["i-144"] = w3_s1_max
        self.data["i-158"] = w4_s1_max

        self.data["i-117"] = s1_min
        self.data["i-131"] = s1_min
        self.data["i-145"] = s1_min
        self.data["i-159"] = s1_min

        self.data["i-118"] = w1_s2_max
        self.data["i-132"] = w2_s2_max
        self.data["i-146"] = w3_s2_max
        self.data["i-160"] = w4_s2_max

        self.data["i-119"] = s2_min
        self.data["i-133"] = s2_min
        self.data["i-147"] = s2_min
        self.data["i-161"] = s2_min
        print(f"[INFO] Successfuly applied parameters from the table 3. ---Calculations - line 621---")


    def find_distance_for_bal(self, h_min:float, h_max:float, direction:str) -> float:
        """This functions will calculate the W with our formula.

        Args:
            h_min (float): Minimum of H.
            h_max (float): Maximum of H.
            direction (str): If we are at the up or down.

        Returns:
            float: The W of wall.
        """
        def formula(hmax, hmin):
            return (hmax-hmin)/cos(radians(self.ball_degre)) * self.z_shirvani
        
        h_min_temp = h_min
        d1, d2 = 0, 1
        if direction in ["UP", "up", "Up", "uP"]:
            while abs(d2-d1) > 0.2:
                d1 = formula(hmax=h_max, hmin=h_min_temp)
                h_min_temp = 1 + d1*self.z_natural
                d2 = formula(hmax=h_max, hmin=h_min_temp)
        elif direction in ["DOWN", "down", "Down"]:
            while abs(d2-d1) > 0.2:
                d1 = formula(hmax=h_max, hmin=h_min_temp)
                h_min_temp = 1 - d1*self.z_natural
                d2 = formula(hmax=h_max, hmin=h_min_temp)
        print(f"[INFO] Find the distance in {direction} for min height of {h_min} and max height of {h_max}. and The distance for W is {d2}")
        return d2

    def count_in_pos(self, p:int, count:str, cal=False) -> str:
        """count and return the number for second column in the table of result.

        Args:
            p (int): The posision that we want to decide on. it can be from 1 to 10.
            count (str): The count column of table 2. It can be 3.1 or 3*4.
            cal (bool, optional): If True, it will calucate the result. If false, it will return in the same format as input. Defaults to False.

        Returns:
            str: Counted number.
        """
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
            elif p in [3, 5, 6, 8, 9]:
                if count_p2:
                    if cal:
                        return str(ceil(float(count_p1)) * int(count_p2))
                    else:
                        return str(ceil(float(count_p1))) + "*" + count_p2
                else:
                    return str(ceil(float(count_p1)))
            else:
                print("[ERROR] There is a problem with p. ---Calculation - line 541---")
                return "Problem accured"
        
    def weight_in_pos(self, D:float, L:float=None, dec:int=1) -> float:
        """Return the weight for us.

        Args:
            D (float): Diameter in mm for the position.
            L (float, optional): If Null it will count the weight for 1 meter. If it numbered it will calculate the total weight for us. Defaults to None.
            dec (int, optional): Decimal. Defaults to 1.

        Returns:
            float: The weight or total weight.
        """
        if D == "-":
            return "-"
        else:
            if L:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res*L, dec)
            else:
                res = ((pi*(D/1000)**2)/4)*7850
                return round(res, dec)
    
    def lengh_in_pos(self, p:int=None, D:str=None, N:str=None, L:str=None, dec:int=1) -> float:
        """Give us the lenght item in table.

        Args:
            p (int, optional): The selected posision. Defaults to None.
            D (str, optional): p-diameter in table. Defaults to None.
            N (str, optional): Count. Defaults to None.
            L (str, optional): p-L in table. Defaults to None.
            dec (int, optional): decimal. Defaults to 1.

        Returns:
            float: The lenght in result table.
        """
        L = float(L)
        N = float(N)
        D = float(D) 

        if p in [1, 2, 4, 7, 8, 9, 10]:
            if N:
                return round(L*N, dec)
            else:
                return round(L, dec)
            
        elif p in [3, 5, 6]:
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

            
