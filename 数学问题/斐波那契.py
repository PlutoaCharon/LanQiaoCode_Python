'''
1.
斐波那契数列前n项之和等于
f(n+2)-1
Sn=2a(n)+a(n-1)-1
每60个一循环

2.
from functools import lru_cache
@lru_cache(None)

3.
矩阵乘法求斐波那契
'''
def fib(n):
    if n == 1 or n == 2:
        return 1

    a = 1
    b = 1
    c = 0
    for i in range(3, n+1):
        c = a+b
        a = b
        b = c
    return c
