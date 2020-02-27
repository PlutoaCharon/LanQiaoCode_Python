def dfs(x, y, step):
    if step > 3 or x < 0 or y < 0 or x > n-1 or y > m-1:
        return
    arr[x][y] = '#'
    for i in range(8):
        dfs(x + dir[i][0], y + dir[i][1], step + 1)
if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    arr = [['.' for j in range(m)] for i in range(n)]
    dir = [[-2,-1],[1,2],[-1,-2],[2,1],[2, -1],[1,-2],[-1,2],[-2,1]]

    dfs(x-1,y-1,0)

    for i in range(n):
        for j in range(m):
            print(arr[i][j], end='')
        print()