from collections import defaultdict

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dic = defaultdict(int)
n = int(input())


def dfs1(x, y, step, path):
    if x + y == n - 1:
        dic[path] = 1
        vis[x][path] = 1
        return

    for i in range(0, 2):
        if x + dx[i] < n and x + dx[i] >= 0 and y + dy[i] < n and y + dy[i] >= 0:
            dfs1(x + dx[i], y + dy[i], step + 1, path + mp[x + dx[i]][y + dy[i]])


ans = int(0)


def dfs2(x, y, step, path):
    global ans

    if x + y == n - 1:
        if dic[path] == 1 and vis[x][path] == 1:
            ans += 1
            dic[path] = 0
        return

    for i in range(2, 4):
        if x + dx[i] < n and x + dx[i] >= 0 and y + dy[i] < n and y + dy[i] >= 0:
            dfs2(x + dx[i], y + dy[i], step + 1, path + mp[x + dx[i]][y + dy[i]])


mp = [str("") for i in range(n)]
vis = [defaultdict(int) for j in range(n)]
for i in range(0, n):
    mp[i] = input()

dfs1(0, 0, 1, "" + mp[0][0])

dfs2(n - 1, n - 1, 1, "" + mp[n - 1][n - 1])
print(ans)