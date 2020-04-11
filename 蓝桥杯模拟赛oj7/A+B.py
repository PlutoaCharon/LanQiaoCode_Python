ans = ""
a, b = map(str, input().split())
n = len(str(a))
for i in range(n):
    ans += str(min(int(a[i]), int(b[i])))

print(int(ans))
