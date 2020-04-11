vis = [False for i in range(80010)]
vis[0], vis[1] = True, True
prime = []
for i in range(2, 80000):
    if vis[i] == False:
        prime.append(i)
        for j in range(2, 80000 // i + 1):
            vis[i * j] = True
tot = len(prime)
n = int(input())
ans = 0
for i in range(0, tot):
    for j in range(i, tot):
        k = n - prime[i] - prime[j]
        if k < prime[j]:
            break
        if vis[k] == False:
            ans = ans + 1
print(ans)