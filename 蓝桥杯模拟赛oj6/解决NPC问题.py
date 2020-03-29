import datetime
for i in range(2, 3000):
    today1 = datetime.datetime(i,1,1)
    today2 = datetime.datetime(i+1,1,1)
    resultDay = today1 + datetime.timedelta(days=300)
    resultDay2 = today2 + datetime.timedelta(days=200)
    if resultDay.weekday() == 1 and resultDay2.weekday() == 1:
        today3 = datetime.datetime(i-1, 1, 1)
        ans = today3 + datetime.timedelta(days=100)
        print(ans.weekday())

