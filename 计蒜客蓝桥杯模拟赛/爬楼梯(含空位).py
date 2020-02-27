'''
蒜头要爬楼梯。楼梯一共有 10 层台阶。因为腿长的限制，每次最多能上 4 层台阶。但是第 5,7层楼梯坏掉了不能踩。求上楼梯的方案数
https://nanti.jisuanke.com/t/43116
'''
ans = [0]*11 # 定义存放数据的列表
ans[0] = 1 # 初始化
for i in range(1, 11):
    if i == 5 or i == 7:
        continue
    if i - 1 >= 0:
        ans[i] += ans[i-1]
    if i - 2 >= 0:
        ans[i] += ans[i-2]
    if i - 3 >= 0:
        ans[i] += ans[i-3]
    if i - 4 >= 0:
        ans[i] += ans[i-4]
print(ans)