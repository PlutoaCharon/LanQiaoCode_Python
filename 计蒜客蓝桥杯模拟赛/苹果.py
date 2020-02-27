count = 0
list = [7 ,2 ,12, 5, 9, 9, 8, 10, 7, 10 ,5 ,4 ,5, 8, 4, 4, 10, 11, 3 ,8 ,7 ,8, 3, 2, 1, 6, 3, 9, 7, 1,0,0]
for i in range(30):
    if list[i] >=  3:
        count += list[i] // 3
        list[i] = list[i] % 3
    flag = True
    while flag:
        if list[i] >=1 and list[i + 1] >= 1 and list[i + 2] >= 1:
            count += 1
            list[i] -= 1
            list[i + 1] -= 1
            list[i + 2] -= 1
        else:
            flag = False
print(list)
print(count)