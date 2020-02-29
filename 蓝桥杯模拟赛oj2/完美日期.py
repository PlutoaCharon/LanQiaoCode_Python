y = 2020
m = 2
d = 2
day_ = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
ans = 0
while ans <= 87:
    if '4' not in str(y) and '4' not in str(d) and '4' not in str(m):
        if d >= 10:
            if (y+m+int(str(d)[0])+(int(str(d)[1]))) % 8 == 0:
                ans += 1
                print(ans)
                print(y, m, d)
        else:
            if (y+m+d)%8 == 0:
                ans += 1
                print(ans)
                print(y, m, d)
    d += 1
    if d > day_[m]:
        d = 1
        m += 1
    if m > 12:
        m = 1
        y += 1


