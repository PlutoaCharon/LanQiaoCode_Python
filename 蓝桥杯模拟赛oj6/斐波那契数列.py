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

if __name__ == '__main__':
    ans = fib(202003281331)
    print(ans)
    print(list(ans)[-1])