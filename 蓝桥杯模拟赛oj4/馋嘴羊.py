def dfs(x, y):
    if x < 0 or y < 0 or x > n - 1 or y > m - 1 or vis[x][y] == 1 or arr[x][y] == '0':
        return
    vis[x][y] = 1
    global ans
    ans += 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

if __name__ == '__main__':
    n, m ,x, y= map(int, input().split())

    arr = []
    for i in range(n):
        str = input()
        arr.append(list(str))

    vis = [[0 for _ in range(m)] for _ in range(n)] # 判断是否走过,0为未走过,1为走过
    ans = 0

    dfs(x,y)


    print(ans)