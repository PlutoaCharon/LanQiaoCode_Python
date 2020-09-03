'''
2 16
10001111
815
'''


# def f(num, n):
#     res = ''
#     while True:
#         a, b = divmod(num, n)
#         res = str(b) + res
#         if a == 0:
#             break
#         num = a
#     return res
# A,B = map(int, input().split())
# n = int(input())
# n = int(str(n), A)
# ans = f(n, B)
# print(ans)

def f(n, x):
    # n为待转换的十进制数，x为机制，取值为2-16
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    b = []
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    ans = ''
    for i in b:
        ans += str(a[i])
    return ans


A, B = map(int, input().split())
n = int(input())
n = int(str(n), A)
ans = f(n, B)
print(ans)
