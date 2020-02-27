n = int(input())
value = 0
list = list(map(int, input().split()))

for i in range(n - 1):
    list = sorted(list)
    value += list[0] + list[1]
    value_list = list[0] + list[1]
    list.pop(0)
    list.pop(0)
    list.append(value_list)
print(value)