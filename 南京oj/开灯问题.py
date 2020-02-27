'''
有 n 盏灯，编号为 1∼n. 第 1 个人把所有灯打开，第 2 个人按下所有编号为 2 的倍数的开关 (这些灯被关掉) , 第 3 个人按下所有编号为 3 的倍数的开关 (其中关掉的灯将被打开，打开的将被关掉) , 依次类推。一共有 k 个人，问最后有哪些灯开着？
样例输入
7 3
样例输出
1
5
6
7
'''
n, k = map(int, input().split())
light_list = [True for i in range(n+1)]
for i in range(2, k+1):
    for j in range(1, n+1):
        if j % i == 0:
            if light_list[j] == True:
                light_list[j] = False
            else:
                light_list[j] = True
for i in range(1, n+1):
    if light_list[i] == True:
        print(i)