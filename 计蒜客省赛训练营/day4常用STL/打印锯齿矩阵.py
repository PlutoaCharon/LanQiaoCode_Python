'''
锯齿矩阵是指每一行包含的元素个数不相同的矩阵，比如：
3 5 2 6 1
2 3 4
1 6 2 7
读入若干对整数 (x,y)，表示在第 x 行的末尾加上一个元素 y。输出最终的锯齿数组。初始时矩阵为空。
输入格式
第一行输入两个整数n,m(1≤n,m≤10000)，其中 n 表示锯齿数组的行数，m 表示插入的元素总数。
接下来一共 m 行，每行两个整数 x,y(1≤x≤n,0≤y≤10000)，表示在第 x 行的末尾插入一个元素 y。
输出格式
一共输出 n 行，每行若干个用空格分隔的整数。如果某行没有任何元素，则输出一个空行。
样例输入
3 12
1 3
2 2
2 3
2 4
3 1
3 6
1 5
1 2
1 6
3 2
3 7
1 1
样例输出
3 5 2 6 1
2 3 4
1 6 2 7
'''

n, m = map(int, input().split())
ans_arr = [[] for _ in range(n)]

# 输入数据
for i in range(m):
    x,y = map(int, input().split())
    ans_arr[x-1].append(y)

# 输出数组
for i in range(n):
    for j in range(len(ans_arr[i])):
        print(ans_arr[i][j], end=' ')
    print()