'''
题意：输入一个n,接下来有n-1行。
输入父亲和儿子
求n个人,每个人的直系后代有多少

输入:
4
1 2
1 3
2 4

输出:
1 3
2 1
3 0
4 0
'''
def dfs(u):
    cnt = 0
    for i in range(len(son[u])):
        cnt += dfs(son[u][i])
    ans[u] = cnt
    return cnt + 1

if __name__ == '__main__':
    n = int(input())
    son = [[] for _ in range(n+1)] # 存放各个父辈的孩子
    ans = [0 for _ in range(n+1)]
    f = [0 for _ in range(n+1)]    # 非True即为祖宗
    for i in range(n-1):
        x,y = map(int, input().split())
        son[x].append(y)
        f[y] = True
    for i in range(1, n+1):
        if f[i] != True:
            u = i                    # 找到祖宗
            break
    dfs(u)
    for i in range(1, n+1):
        print(i, ans[i])


