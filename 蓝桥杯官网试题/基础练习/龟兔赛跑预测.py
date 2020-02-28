data = list(map(int, input().split()))
rabbit = turtle = 0
time = 0 #目前的时间
flag = False
while True:
    if  rabbit == data[-1] or turtle == data[-1]: # 到达终点
        break
    if  rabbit - turtle >= data[2]:
        for i in range(data[3]):
            turtle += data[1]
            time += 1
            if turtle >= data[-1]:
                flag = True
                break
        if flag:
            break

    time += 1
    rabbit += data[0]
    turtle += data[1]

if rabbit > turtle:  # 谁先到达终点，谁的距离大
    print('R')
    print(time)
elif rabbit < turtle:
    print('T')
    print(time)
else:  # 相等则平局
    print('D')
    print(time)
