'''
问题描述
　　对于一个 n 行 m 列的表格，我们可以使用螺旋的方式给表格依次填上正整数，我们称填好的表格为一个螺旋矩阵。
　　例如，一个 4 行 5 列的螺旋矩阵如下：
　　1 2 3 4 5
　　14 15 16 17 6
　　13 20 19 18 7
　　12 11 10 9 8
输入格式
　　输入的第一行包含两个整数 n, m，分别表示螺旋矩阵的行数和列数。
　　第二行包含两个整数 r, c，表示要求的行号和列号。
输出格式
　　输出一个整数，表示螺旋矩阵中第 r 行第 c 列的元素的值。
样例输入
4 5
2 2
样例输出
15
评测用例规模与约定
　　对于 30% 的评测用例，2 <= n, m <= 20。
　　对于 70% 的评测用例，2 <= n, m <= 100。
　　对于所有评测用例，2 <= n, m <= 1000，1 <= r <= n，1 <= c <= m。
'''
n, m = map(int, input().split())
r, c = map(int, input().split())
ansList = [[0 for _ in range(m)] for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]
i = 1
x = 0  # 当前纵坐标
y = 0  # 当前横坐标
while i < n * m:

    while y < m and vis[x][y] == 0:
        ansList[x][y] = i
        vis[x][y] = 1
        i += 1
        y += 1

    y -= 1
    x += 1

    while x < n and vis[x][y] == 0:
        ansList[x][y] = i
        vis[x][y] = 1
        i += 1
        x += 1

    x -= 1
    y -= 1

    while y >= 0 and vis[x][y] == 0:
        ansList[x][y] = i
        vis[x][y] = 1
        i += 1
        y -= 1

    y += 1
    x -= 1

    while x >= 0 and vis[x][y] == 0:
        ansList[x][y] = i
        vis[x][y] = 1
        i += 1
        x -= 1
    x += 1
    y += 1
print(ansList[r-1][c-1])













