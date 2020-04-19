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













