import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Grades:
    def __init__(self, name:str):
        self.name = name
        self.data_project = pd.DataFrame(columns=["first_name", "last_name", "id", "p1(10+2.5)", "p2(10)", "p3(5)", "p4(5)", "p5(35)", "p6(10)", "p7(25)"])
        self.data_train = pd.DataFrame(columns=["first_name", "last_name", "id", "T1()", "T2()", "T3()"])
        self.data_final = pd.DataFrame(columns=["first_name", "last_name", "id", "q1(60)", "q2(40)"])
        self.data_present = pd.DataFrame(columns=["first_name", "last_name", "id", "g"])
        
    def add_new_project_student(self, first_name, last_name, id,
                p1, p2, p3, p4, p5, p6, p7):
        columns = list(self.data_project.columns)
        self.data_project.loc[len(self.data_project)] = {columns[0]: first_name,
                                         columns[1]: last_name,
                                         columns[2]: id,
                                         columns[3]: p1,
                                         columns[4]: p2,
                                         columns[5]: p3,
                                         columns[6]: p4,
                                         columns[7]: p5,
                                         columns[8]: p6,
                                         columns[9]: p7}
        
    def add_new_train_student(self, first_name, last_name, id,
                t1, t2, t3):
        columns = list(self.data_train.columns)
        self.data_train.loc[len(self.data_train)] = {columns[0]: first_name,
                                         columns[1]: last_name,
                                         columns[2]: id,
                                         columns[3]: t1,
                                         columns[4]: t2,
                                         columns[5]: t3}
        
    def add_new_final_student(self, first_name, last_name, id,
                q1, q2):
        columns = list(self.data_final.columns)
        self.data_final.loc[len(self.data_final)] = {columns[0]: first_name,
                                         columns[1]: last_name,
                                         columns[2]: id,
                                         columns[3]: q1,
                                         columns[4]: q2}
        
    def add_new_presentation_student(self, first_name, last_name, id,
                                     g):
        columns = list(self.data_present.columns)
        self.data_present.loc[len(self.data_present)] = {columns[0]: first_name,
                                         columns[1]: last_name,
                                         columns[2]: id,
                                         columns[3]: g}
        
    def calculate_grades(self):
        self.data_project["sum(100)"] = self.data_project.iloc[:, 3:].sum(axis=1)
        self.data_train["sum(100)"] = self.data_train.iloc[:, 3:].sum(axis=1)
        self.data_final["sum(100)"] = self.data_final.iloc[:, 3:].sum(axis=1)
