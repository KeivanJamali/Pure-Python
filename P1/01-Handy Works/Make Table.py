from tabulate import tabulate

header = ["Course_Name", "Date", "Exam_Time", "Lecturer", "basket", "vahed"]
data = [
    ["roszi", "1,3,4 13:30 to 15, 10 to 12:30", "2/4 9:00", "sabori", 0, 3],
    ["zirsakht", "0,2 from 10:30 to 12", "26/3, 15:30", "kermanshah", 1, 3],
    ["system", "0,2 from 15 to 16:30", "21/3, 9:00", "mosavi", 1, 3],
    ["motale khas", "0,2 from 15 to 16:30", "2/4 9:00", "ahmadi", 1,3],
    ["onvan khas", "1,3 from 9 to 10:30", "27/3 15:30", "mogim", "?",3],
    ["khalagiat", "1,3 from 13 to 14:30", "3/4 9:00", "jamali", "?",3],
]


class Make_Table:
    def __init__(self, data: list, header: list):
        self.data = data
        self.header = header
        print(tabulate(data, headers=header, tablefmt="fancy_grid", showindex="always", numalign="center"))


Make_Table(data, header)
