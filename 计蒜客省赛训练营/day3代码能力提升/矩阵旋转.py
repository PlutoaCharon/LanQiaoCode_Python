'''
输入:
3 4
-1 3 6 3
7 7 9 1
10 3 4 6
输出:
10 7 -1
3 7 3
4 9 6
6 1 3
'''
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_ans = [[0 for i in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        arr_ans[i][j] = arr[n-j-1][i]

for i in range(m):
    for j in range(n):
        print(arr_ans[i][j], end=' ')
    print()