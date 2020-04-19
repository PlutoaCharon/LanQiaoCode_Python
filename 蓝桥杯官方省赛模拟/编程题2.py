n = int(input())
ans = 0
a,b,c = map(int, input().split())
for i in range(1, n+1):
    if i % a != 0 and i % b != 0 and i % c != 0:
        ans += 1
    else:
        continue
print(ans)