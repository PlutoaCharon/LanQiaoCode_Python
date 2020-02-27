n, m = map(int, input().split())
tmp = []
vis = [[0 for i in range(m)] for i in range(n)] # 验证位置是否走过
arr = [list(map(int, input().split())) for _ in range(n)]
# 注意: 向下为x, 向右为y
x = 0 # 当前纵坐标
y = 0 # 当前横坐标
while len(tmp) < n*m :
    while x < n and vis[x][y] == 0:
        tmp.append(arr[x][y])
        vis[x][y] = 1
        x += 1  # 纵坐标加一
    x -= 1 # 将上步多余的步数删除,防止溢出
    y += 1 # 将横坐标右移
    while y < m and vis[x][y] == 0:
        tmp.append(arr[x][y])
        vis[x][y] = 1
        y += 1
    x -= 1 # 将纵坐标减一
    y -= 1 # 将上步多余步数删除,防止溢出
    while x >= 0 and vis[x][y] == 0:
        tmp.append(arr[x][y])
        vis[x][y] = 1
        x -= 1 # 将纵坐标上移
    x += 1 # 将上步多余步数删除,防止溢出
    y -= 1 # 将横坐标左移
    while y >=0 and vis[x][y] == 0:
        tmp.append(arr[x][y])
        vis[x][y] = 1
        y -= 1 # 将横坐标左移
    y += 1 # 将上步多余步数删除
    x += 1 # 将纵坐标下移

# 输出数据
for i in range(len(tmp)):
    print(tmp[i], end=' ')
