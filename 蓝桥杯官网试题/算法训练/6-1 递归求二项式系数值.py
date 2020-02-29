'''
# 方法一 递归
def C(k,n):
    if k == n or k == 0:
        return 1
    else:
        return C(k, n-1)+C(k-1,n-1)

k,n = map(int, input().split())
print(C(k,n))
'''

# 方法二 动态规划
'''
k = 3 n = 10
[0, 0, 0, 0],
[1, 1, 0, 0], 
[1, 2, 1, 0], 
[1, 3, 3, 1], 
[1, 4, 6, 4], 
[1, 5, 10, 10], 
[1, 6, 15, 20], 
[1, 7, 21, 35], 
[1, 8, 28, 56], 
[1, 9, 36, 84], 
[1, 10, 45, 120]
'''
k,n = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# k=0时候, 1填入dp数组中
for i in range(1, n+1):
    dp[i][0] = 1

# k=n时候, 1填入dp数组中
for i in range(1, k+1):
    dp[i][i] = 1

for i in range(2, n+1):
    for j in range(1, k+1):
        if i > j:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n][k])