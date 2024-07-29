import pandas as pd
import os
code_name = "delete_distance_from_centerline"

class Delete_Distance_From_Centerline:
    def __init__(self, main_file, left_bound, right_bound):
        self.data = None
        self.left_modes = None
        self.CSDP = None
        self.file_name = main_file
        self.raw_data_main = pd.read_csv(main_file, header=0)
        self.set_raw_data()
        self.left_bound, self.right_bound= left_bound, right_bound
        
    def set_raw_data(self):
        counted_L = -1
        counted_R = 0
        for i in self.raw_data_main.columns:
            if "L" in i:
                counted_L += 1
            if "R" in i:
                counted_R += 1

        column = ["No", "Distance"]
        column_for_result = ["No", "Distance"]
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
        column_for_result.append("end")
        self.raw_data_main.columns = column
        self.columns_for_result = column_for_result
    
    def use_bounds(self):
        result = pd.DataFrame("empty", index=self.raw_data_main.index, columns=self.columns_for_result)

        for i in range(0, len(self.raw_data_main), 2):
            for j in range(2, len(self.raw_data_main.loc[i])-1):
                node = self.raw_data_main.iloc[i, j]
                if self.raw_data_main.columns[j] in self.left_modes:
                    if (self.left_bound-node) <= 0:
                        result.iloc[i, j] = node
                        result.iloc[i+1, j] = self.raw_data_main.iloc[i+1, j]
                    else:
                        result.iloc[i, j] = "empty"
                        result.iloc[i+1, j] = "empty"
                elif "R" in self.raw_data_main.columns[j]:
                    if (node - self.right_bound) >= 0:
                        result.iloc[i, j] = node
                        result.iloc[i+1, j] = self.raw_data_main.iloc[i+1, j]
                    else:
                        result.iloc[i, j] = "empty"
                        result.iloc[i+1, j] = "empty"

        result["CL"] = self.raw_data_main["CL"]
        result["Distance"] = self.raw_data_main["Distance"]
        result["No"] = self.raw_data_main["No"]
        result["end"] = "empty"
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
    
    @staticmethod
    def shift_empty_columns(df):
        # Get column names
        cols = df.columns
        l_cols = [col for col in cols if col.startswith('L')]
        r_cols = [col for col in cols if col.startswith('R')]
        
        def shift_row(row, cols, direction):
            first_empty = None
            if direction == "right":
                for col in reversed(cols):
                    if first_empty is None and row[col] == 'empty':
                        first_empty = col
                    elif first_empty is not None:
                        row[first_empty] = row[col]
                        first_empty = col
                row[first_empty] = "empty"
            elif direction == "left":
                for col in cols:
                    if first_empty is None and row[col] == 'empty':
                        first_empty = col
                    elif first_empty is not None:
                        row[first_empty] = row[col]
                        first_empty = col
                row[first_empty] = "empty"
            return row
        
        def process_row(row):
            # Process left side columns
            l_continuous_empty = [col for col in l_cols if row[col] == 'empty']
            if len(l_continuous_empty) > 0 and l_continuous_empty[-1] == l_cols[-1]:
                row = shift_row(row, l_cols, 'right')
            
            # Process right side columns
            r_continuous_empty = [col for col in r_cols if row[col] == 'empty']
            if len(r_continuous_empty) > 0 and r_continuous_empty[0] == r_cols[0]:
                row = shift_row(row, r_cols, 'left')
            return row
        
        # Apply processing to each row
        for _ in range(10):
            df = df.apply(process_row, axis=1)
        return df    

    def fit(self):
        result = self.use_bounds()
        result.fillna("", inplace=True)
        result = Delete_Distance_From_Centerline.shift_empty_columns(result)
        result.replace("empty", "", inplace=True)
        self.CSDP = result
        return self.CSDP
    
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