a, b, c = map(int, input().split())
list = []
list.append(1)
for i in range(1, 2000001):
    num = ((a*list[i-1]) + (list[i-1] % b)) % c
    list.append(num)
    if len(list) != len(set(list)):
        print(i)
        break
    else:
        continue

else:
    print(-1)
