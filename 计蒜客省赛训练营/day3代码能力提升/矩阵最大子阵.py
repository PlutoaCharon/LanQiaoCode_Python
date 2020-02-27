'''
矩阵本身可看作是一个特殊的子矩阵
输入:
3 3
2 -4 1
-1 2 1
4 -2 2
输出:
6
'''
n, m = map(int, input().split())
arr  = [list(map(int, input().split())) for _ in range(n)]
ans  = 0
for i in range(n):
    for j in range(i, n):
        for k in range(m):
            for l in range(k, m):
                tmp = 0
                for p in range(i, j+1):
                    for q in range(k, l+1):
                        tmp += arr[p][q]
                if tmp > ans:
                    ans = tmp
print(ans)