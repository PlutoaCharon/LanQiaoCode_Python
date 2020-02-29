k, l = map(int, input().split())
mod = 1000000007
ans = 0
dp = [[0 for _ in range(l+1)] for _ in range(k)]

for i in range(k):
    dp[i][1] = 1

for i in range(2, l+1): # 按列遍历 l表示l位数
    for j in range(k):  # 按行遍历
        for w in range(k):
            if w != j+1 and w != j-1: # 相邻的数字不添加
                dp[j][i] = (dp[j][i] + dp[w][i-1])%mod

# 将第l列的数字相加即为ans
for i in range(1,k):
    ans = (ans + dp[i][l])%mod

print(ans)

