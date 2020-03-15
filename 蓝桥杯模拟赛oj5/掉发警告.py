ans = 0
n = int(input())
list = [0, 1, 2, 3, 5]
if n == 1 or n == 2 or n == 3 or n == 4:
    ans = list[n]
else:
    for i in range(5, n + 1):
        tmp = list[i - 3] + list[i - 1] + 1
        list.append(tmp)
    ans = list[-1]
print(ans)