ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
n = int(input())
arr = list(map(str, input()))

for i in range(0, n, 2):
    # tmp = arr[:]
    if arr[i] != "R":
        ans1 += 1
    if arr[i] != "L":
        ans2 += 1

for i in range(1, n, 2):
    if arr[i] != "L":
        ans1 += 1
    if arr[i] != "R":
        ans2 += 1

for i in range(n // 2):
    if arr[i] != "R":
        ans3 += 1
    else:
        ans4 += 1

for i in range(n // 2, n):
    if arr[i] != "L":
        ans3 += 1
    else:
        ans4 += 1
print(min(ans1, ans2, ans3, ans4))
