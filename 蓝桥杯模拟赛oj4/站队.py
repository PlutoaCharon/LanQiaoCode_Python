n = int(input())
data = []
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    tmp.append(i)
    data.append(tmp)

data = sorted(data,key=lambda x:x[1])
data = sorted(data,key=lambda x:x[0])

for i in range(n-1):
    print(data[i][2], end=" ")
print(data[n-1][2])