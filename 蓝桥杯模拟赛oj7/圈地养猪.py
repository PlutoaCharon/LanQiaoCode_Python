n = int(input())
listX = []
listY = []
for i in range(n):
    x, y = map(int, input().split())
    listX.append(x)
    listY.append(y)
listX = sorted(listX)
listY = sorted(listY)
minX = listX[0]
maxX = listX[-1]
minY = listY[0]
maxY = listY[-1]

ans = ((maxX - minX + 2) + (maxY - minY + 2)) * 2
print(ans)
