n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [True] * n
for i in range(n):
    count = 0
    for j in range(n):
        if arr[j][i] == 0:
            count += 1
        if count >= n/2:
            tmp[i] = False
            break
for i in range(n):
    if tmp[i]:
        print(i+1, end=' ')
