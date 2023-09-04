"""how many days in a year?"""
"""Thirty days = April, June, November, September
thirty-one = January, March, May, July, August, October, December
twenty-eight / twenty-nine = February
2020 is leap year
leap year = 366
a year = 365
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")"""
import datetime

befor_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
befor_days2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]


def if_is_leap(year: int) -> bool:
    if divmod(year, 4)[1] == 0:
        return True
    else:
        return False


def find_days(date1: list, date2: list) -> int:
    """find days between two date"""
    # convert years to days
    temp = 0
    for i in range(date1[0], date2[0]):
        if if_is_leap(i) == True:
            temp += 366
        else:
            temp += 365
    days = temp
    # convert month to days
    if if_is_leap(date2[0]) == True:
        temp2 = befor_days2[date2[1] - 1]
    else:
        temp2 = befor_days[date2[1] - 1]
    if if_is_leap(date1[0]) == True:
        temp1 = befor_days2[date1[1] - 1]
    else:
        temp1 = befor_days[date1[1] - 1]
    days = days + temp2 - temp1
    # add days to them
    days = days + date2[2] - date1[2]
    # print(days)
    return days


def main(i):
    date1 = [1901, 1, 1]  # input
    date1_day = datetime.date(1901, 1, 1).weekday()
    # print(date1_day)
    date2 = [2000, 12, 31]  # input
    days = find_days(date1, date2) + date1_day
    week, day = divmod(days, 7)
    if i >= date1_day:
        if i <= day:
            week += 1
    else:
        if i > day:
            week -= 1
    return week


print(main(6))
