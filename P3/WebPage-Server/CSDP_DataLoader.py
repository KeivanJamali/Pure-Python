import pandas as pd
import os
code_name = "CSDP"

class CSDP_DataLoader:
    def __init__(self, main_file, second_ground_file, pashneh_file):
        self.data = None
        self.left_modes = None
        self.result_without_additionals = None
        self.CSDP = None
        self.file_name = main_file
        self.raw_data_main = pd.read_csv(main_file, header=0)
        self.raw_data_pashneh = pd.read_csv(pashneh_file, header=3)
        self.raw_data_second = pd.read_csv(second_ground_file, header=3)
        self.set_raw_data()
        self.left_bound, self.right_bound, self.additionals = self.boundry_maker()
        

    def set_raw_data(self):
        counted_L = -1
        counted_R = 0
        for i in self.raw_data_main.columns:
            if "L" in i:
                counted_L += 1
            if "R" in i:
                counted_R += 1

        column = ["No", "Distance"]
        column_for_result = ["No", "Distance", f"L{counted_L+3}", f"L{counted_L+2}", f"L{counted_L+1}"]
        self.left_modes = []
        for i in range(counted_L, 0, -1):
            column.append(f"L{i}")
            column_for_result.append(f"L{i}")
            self.left_modes.append(f"L{i}")
        column.append("CL")
        column_for_result.append("CL")
        for i in range(1, counted_R+1):
            column.append(f"R{i}")
            column_for_result.append(f"R{i}")
        column.append("end")
        column_for_result.append(f"R{counted_R+1}")
        column_for_result.append(f"R{counted_R+2}")
        column_for_result.append(f"R{counted_R+3}")
        column_for_result.append("end")
        self.raw_data_main.columns = column
        self.columns_for_result = column_for_result


    def boundry_maker(self):
        additionals = self.end_nodes()
        bound_l = []
        bound_r = []
        for row in range(0, len(self.raw_data_second), 2):
            done = False
            for row_temp in range(0, len(self.raw_data_main), 2):
                if self.raw_data_second["Distance"][row] == self.raw_data_main["Distance"][row_temp]:
                    bound_l.append(self.raw_data_second["L3"][row])
                    bound_l.append(self.raw_data_second["L3"][row+1])
                    bound_r.append(self.raw_data_second["R3"][row])
                    bound_r.append(self.raw_data_second["R3"][row+1])
                    additionals.loc[row] = self.raw_data_pashneh[additionals.columns].loc[row]
                    additionals.loc[row+1] = self.raw_data_pashneh[additionals.columns].loc[row+1]
                    done = True
                if done:
                    break
            if done:
                continue
            else:
                print(row, row_temp)
                bound_l.append("empty")
                bound_l.append("empty")
                bound_r.append("empty")
                bound_r.append("empty")

        additionals.fillna("empty", inplace=True)
        return bound_l, bound_r, additionals
    
    def end_nodes(self):
        temp_additional = ["L3", "L4", "L5", "R3", "R4", "R5"]
        additional = []
        for add in temp_additional:
            if add in self.raw_data_pashneh.columns:
                additional.append(add)
        return pd.DataFrame("empty", index=range(len(self.raw_data_main)), columns=additional)
        # additional_pashneh = self.raw_data_pashneh[additional]
        # return additional_pashneh
    
    def use_bounds(self):
        result = pd.DataFrame("empty", index=self.raw_data_main.index, columns=self.columns_for_result)

        for i in range(0, len(self.raw_data_main), 2):
            if self.left_bound[i]:
                for j in range(2, len(self.raw_data_main.loc[i])-1):
                    # print(j)
                    node = self.raw_data_main.iloc[i, j]
                    # print(self.raw_data_main.columns[j])
                    # print(node)
                    # print(self.left_modes)
                    # print((left_bound[i]-node) >= 0)
                    # 0.02
                    if self.raw_data_main.columns[j] in self.left_modes:
                        if (self.left_bound[i]-node) >= 0.01:
                            # print(f"adding {i}-{j}-{data.columns[j]}")
                            result.iloc[i, j+3] = node
                            result.iloc[i+1, j+3] = self.raw_data_main.iloc[i+1, j]
                        else:
                            result.iloc[i, j+3] = "empty"
                            result.iloc[i+1, j+3] = "empty"
                    elif "R" in self.raw_data_main.columns[j]:
                        if (node - self.right_bound[i]) <= 0.01:
                            result.iloc[i, j+3] = node
                            result.iloc[i+1, j+3] = self.raw_data_main.iloc[i+1, j]
                        else:
                            result.iloc[i, j+3] = "empty"
                            result.iloc[i+1, j+3] = "empty"

        result["CL"] = self.raw_data_main["CL"]
        result["Distance"] = self.raw_data_main["Distance"]
        result["No"] = self.raw_data_main["No"]
        result["end"] = 0
        self.result_without_additionals = result
        self.CSDP = result.copy()
        return result
    
    def add_additional_bounds(self):
        for row in range(0, len(self.additionals), 2):
            for col in range(len(self.additionals.columns)):
                if not self.additionals.iloc[row, col] == "empty":
                    if self.additionals.columns[col][0] == "R":
                        for i in range(1, 11):
                            if self.CSDP.loc[row]["R" + str(i)] == "empty":
                                col_i = list(self.CSDP.columns).index("R" + str(i))
                                self.CSDP.iloc[row, col_i] = self.additionals.iloc[row, col]
                                self.CSDP.iloc[row+1, col_i] = self.additionals.iloc[row+1, col]
                                break
                        
                    elif self.additionals.columns[col][0] == "L":
                        for i in range(1, 11):
                            if self.CSDP.loc[row]["L" + str(i)] == "empty":
                                col_i = list(self.CSDP.columns).index("L" + str(i))
                                self.CSDP.iloc[row, col_i] = self.additionals.iloc[row, col]
                                self.CSDP.iloc[row+1, col_i] = self.additionals.iloc[row+1, col]
                                break
        return self.CSDP
    
    def add_left_right_bounds(self):
        for row in range(0, len(self.left_bound), 2):
            if not self.right_bound[row] == "empty":
                for i in range(1, 11):
                    if self.CSDP.loc[row]["R" + str(i)] == "empty":
                        col_i = list(self.CSDP.columns).index("R" + str(i))
                        self.CSDP.iloc[row, col_i] = self.right_bound[row]
                        self.CSDP.iloc[row+1, col_i] = self.right_bound[row+1]
                        break
                
            if not self.left_bound[row] == "empty":
                for i in range(1, 11):
                    if self.CSDP.loc[row]["L" + str(i)] == "empty":
                        col_i = list(self.CSDP.columns).index("L" + str(i))
                        self.CSDP.iloc[row, col_i] = self.left_bound[row]
                        self.CSDP.iloc[row+1, col_i] = self.left_bound[row+1]
                        break
    
    def fit(self):
        result_without_additionals = self.use_bounds()
        self.add_left_right_bounds()
        result = self.add_additional_bounds()
        result.fillna("", inplace=True)
        result.replace("empty", "", inplace=True)
        for col in result.columns:
            if not result[col].astype(str).sum():
                result.drop(columns=col, inplace=True)
        return result
    
    def save_files(self, folder_name:str) -> tuple[str]:
        """
        Save the processed data to CSV and text files in the specified folder.

        Parameters:
        folder_name (str): The path to the folder where the files will be saved.

        Returns:
        tuple: Paths to the saved CSV, text, out-of-range, and zeros files.
        """
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]

        # Save the CSV file
        csv_file = os.path.join(folder_name, f"{code_name}_{base_name}")
        self.CSDP.columns = list(self.CSDP.columns[0:2]) + [i[0] if i!="CL" else "CL" for i in self.CSDP.columns[2:]]
        self.CSDP.to_csv(csv_file, index=False, header=True)

        return csv_file