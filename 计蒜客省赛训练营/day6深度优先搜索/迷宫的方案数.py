'''
输入:
5 5
s####
.####
.####
.####
....e

输出:
1
'''
def dfs(x,y):
    if x > n - 1 or y > m - 1 or x < 0 or y < 0 or vis[x][y] == 1 or maze[x][y] == '#':
        return

    if maze[x][y] == 'e':
        global ans
        ans += 1
        return

    vis[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    vis[x][y] = 0     # 将走过的路删除



if __name__ == '__main__':
    n,m = map(int, input().split())
    # 输入迷宫
    maze = []
    vis = [[0 for _ in range(m)] for _ in range(n) ]
    ans = 0

    for _ in range(n):
        val = input()
        maze.append(list(val))
    # 起始坐标
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 's':
                x = i
                y = j
                break
        else:
            continue
        break

    dfs(x,y)
    print(ans)