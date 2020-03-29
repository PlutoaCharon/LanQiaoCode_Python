arr = [int(input()) for _ in range(10)]
ans = []
cnt = 0

for i in arr:
    tmp = str(i % 42)
    for j in range(len(tmp)):
        ans.append(tmp[j])

ans = set(ans)
cnt = len(ans)
print(cnt)
