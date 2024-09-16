import pandas as pd
import numpy as np

days = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهار شنبه"]
courses = []
courses.append([["مهندسی ترافیک پیشرفته", "امینی"], [1, 3], [10.5, 12], ["1403/10/24", 9]])
courses.append([["تحقیق در عملیات", "شفاهی"], [0, 2], [10.5, 12.5], ["1403/10/26", 15]])
courses.append([["برنامه ریزی حمل و نقل", "شفاهی"], [0, 2], [9, 10.5], ["1403/10/22", 9]])
courses.append([["سمینار حمل و نقل", "کرمانشاه"], [2], [13, 15], ["-", "-"]])
# courses.append([["یادگیری ماشین", "شریفی زارچی"], [1, 3], [9, 10.5], ["1403/11/2", 9]])

data_classes = pd.DataFrame(0, index=np.arange(9, 17, 0.5), columns=days)

exams = [i[3][0] for i in courses]
data_exams = pd.DataFrame(0, index=exams, columns=["9", "15"])


for course in courses:
    row_start = course[2][0]
    row_end = course[2][1]
    cols = [days[i] for i in course[1]]
    name = course[0][0]+" /// "+course[0][1]
    exam_row = course[3][0]
    exam_col = course[3][1]

    data_classes.loc[row_start:row_end, cols] = name
    data_exams.loc[exam_row, exam_col] = name
