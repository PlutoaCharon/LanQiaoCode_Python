def isPrime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


count = 0
for i in range(2, 201):
    if isPrime(i):
        count += 1
        print(i)
print(count)