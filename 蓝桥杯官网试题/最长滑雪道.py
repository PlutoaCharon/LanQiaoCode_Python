def dfs(x, y):
    max_height = 1
    if dp[x][y] > 0:
        return dp[x][y]
    for k in range(4):
        tx = x + next_[k][0]
        ty = y + next_[k][1]
        if tx < 0 or tx >= row or ty < 0 or ty >= col:
            continue
        if arr[tx][ty] >= arr[x][y]:
            continue
        max_height = max(max_height, dfs(tx, ty) + 1)

    dp[x][y] = max_height
    return dp[x][y]

if __name__ == '__main__':
    ans = 0
    row, col = map(int, input().split())
    dp = [[0 for _ in range(col)] for _ in range(row)]
    arr = [list(map(int, input().split())) for _ in range(row)]

    next_ = [[0, 1], [1,0], [0,-1], [-1, 0]]

    for i in range(row):
        for j in range(col):
            ans = max(ans, dfs(i, j))

    print(ans)