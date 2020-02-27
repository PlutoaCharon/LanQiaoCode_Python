'''
小乐乐上课需要走n阶台阶，因为他腿比较长，所以每次可以选择走一阶或者走两阶，那么他一共有多少种走法？
'''
n = int(input())

a = 1
b = 1
c = 0

if n == 1:
    print(a)
elif n == 2:
    print(a + b)
else:
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(c)