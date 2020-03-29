def mybin(x):
    return bin(x).replace('0b', '').zfill(8)


n, m, k = map(int, input().split())
for i in range(n):
    tmp = mybin(i)
