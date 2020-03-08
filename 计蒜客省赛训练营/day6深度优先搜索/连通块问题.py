def dfs(grid, i, j):
    if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '.': return
    grid[i][j] = '.'
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i + 1, j + 1)
    dfs(grid, i - 1, j + 1)
    dfs(grid, i - 1, j - 1)
    dfs(grid, i + 1, j - 1)

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        str = input()
        arr.append(list(str))

    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                dfs(arr,i, j)
                ans += 1
    print(ans)


