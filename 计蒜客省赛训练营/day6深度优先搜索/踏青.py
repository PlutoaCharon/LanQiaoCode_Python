'''
5 6
.#....
..#...
..#..#
...##.
.#....

5 6
. # . . . .
. . # . . .
. . # . . #
. . . # # .
. # . . . .
'''
def dfs(x, y):
    if x < 0 or y < 0 or x > n - 1 or y > m - 1 or vis[x][y] == 1 or arr[x][y] == '.':
        return
    vis[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    # 当输入中有空格分隔开时
    arr = [list(map(str, input().split())) for _ in range(n)]
    # 当输入没有空格分隔开时

    # arr = []
    # for i in range(n):
    #     str = input()
    #     arr.append(list(str))
    vis = [[0 for _ in range(m)] for _ in range(n)] # 判断是否走过,0为未走过,1为走过
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and arr[i][j] == '#':
                dfs(i,j)
                ans += 1
    print(ans)