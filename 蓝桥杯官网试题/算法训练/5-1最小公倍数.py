'''
问题描述
　　编写一函数lcm，求两个正整数的最小公倍数。
样例输入
一个满足题目要求的输入范例。
例：

3 5
样例输出
15
'''
# 最小公倍数 lcm = a*b/gcd(a,b)
# gcd为最大公约数
def gcd(a,b):
    c = a % b
    while c!=0:
        a = b
        b = c
        c = a % b
    return b

if __name__ == '__main__':
    a,b = map(int, input().split())
    lcm = a*b/gcd(a,b)
    print(int(lcm))