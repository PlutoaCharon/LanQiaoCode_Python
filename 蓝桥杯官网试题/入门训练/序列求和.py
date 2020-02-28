def sum():
    n = int(input())
    return n*(1+n)/2 # 等差数列时间短 直接使用a+b会超时
s = int(sum())
print(s)