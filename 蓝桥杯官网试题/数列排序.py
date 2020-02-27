n = int(input())
list = list(map(int, input().split()))
list = sorted(list)
for i in range(len(list)):
    print(list[i], end= ' ')
