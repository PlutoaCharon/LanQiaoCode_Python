# 最大公约数 gcd
# 最小公倍数 lcm = a*b/gcd(a,b)
'''
输入:
2
2 4
3 5

输出:
2
1

'''
n = int(input())


for i in range(n):
    a, b = map(int, input().split())
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    print(b)
