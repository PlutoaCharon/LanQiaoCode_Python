def solve(n):
    tmp = 2
    if tmp == n:
        return True
    while n > tmp:
        k = n % tmp
        if k==0:
            return False
        else:
            tmp += 1
    return True

if __name__ == '__main__':
    count = 0
    for i in range(1, 100000):
        if solve(i) and '5' in str(i):
            count += 1
    print(count)
