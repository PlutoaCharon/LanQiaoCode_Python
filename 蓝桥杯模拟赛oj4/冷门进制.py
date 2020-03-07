# 进制转化
def f(num, n):
    res = ''
    while True:
        a, b = divmod(num, n)
        res = str(b) + res
        if a == 0:
            break
        num = a
    return res

# 输入数据
n = int(input())
nums = list(map(int,input().split()))
num = 0
ans = 0
# 得出相乘的数据
for i in range(1,n):
    num = nums[i] * nums[i-1]
# 转化为列表
num = f(num,6)
num = list(num)
print(num)
for i in range(len(num)):
    if num[-1] == '0':
        ans += 1
        num.pop()
    else:
        break

print(ans)
