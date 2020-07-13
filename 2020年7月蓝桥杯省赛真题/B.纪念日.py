import datetime

d1 = datetime.datetime(1921, 7, 23, 12)
d2 = datetime.datetime(2020, 7, 1, 12)
day = (d2 - d1).days
minute = (d2 - d1).total_seconds() // 60
print(d1, d2)
print(day)
print(minute) # 52038720
