n = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(1,n+1):
    for num in nums:
        if i % num == 0:
            ans += 1
            break
        else:
            continue
print(ans)