year, month, day, k = map(int, input().split())
day_ = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1, k+1):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:   #判断是否为闰年
        day_[2] = 29
    else:
        day_[2] = 28
    day += 1
    if day == day_[month]:
        day = 0
        month += 1
    if month == 13:
        month = 1
        year += 1
print("{:d}-{:0>2d}-{:0>2d}".format(year, month, day))
