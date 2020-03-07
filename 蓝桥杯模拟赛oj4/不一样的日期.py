YY,MM,DD,dd = map(int,input().split())
if dd > 0:
    for i in range(1,dd+1):
        DD += 1
        if DD > 13:
            MM += 1
            DD = 1
        if MM > 23:
            YY += 1
            MM = 1
else:
    for i in range(1,abs(dd)+1):
        DD -= 1
        if DD <= 0:
            MM -= 1
            DD = 13
        if MM <= 0:
            YY -= 1
            MM = 23
print(YY,MM,DD)