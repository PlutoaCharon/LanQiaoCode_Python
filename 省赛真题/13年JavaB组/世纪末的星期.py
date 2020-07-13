from datetime import datetime
week=datetime.strptime("22991231", "%Y%m%d").weekday()
week2=datetime.strptime("20200713", "%Y%m%d").weekday()
print(week) # 6 代表星期日
print(week2)