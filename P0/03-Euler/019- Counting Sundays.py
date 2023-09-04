import datetime


def if_is_someday(date: list, weekday: int) -> bool:
    if datetime.date(date[0], date[1], date[2]).weekday() == weekday:
        return True
    else:
        return False


def main(date1: list, date2: list, weekday: str) -> int:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Tursday", "Friday", "Saturday", "Sunday"]
    for i in range(7):
        if weekdays[i] == weekday:
            weekday_no = i
            break
    sum = 0
    for i in range(date1[0] + 1, date2[0]):
        for j in range(1, 13):
            if if_is_someday([i, j, 1], weekday_no) == True:
                sum += 1
    for i in range(date1[1] + 1, 13):
        if if_is_someday([date1[0], i, 1], weekday_no) == True:
            sum += 1
    for i in range(1, date2[1]):
        if if_is_someday([date1[0], i, 1], weekday_no) == True:
            sum += 1
    return sum


print(main([1901, 1, 1], [2000, 12, 31], "Sunday"))
