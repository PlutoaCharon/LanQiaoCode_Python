data = list(map(float, input().split()))

if data[0] == 0:
    ans = (data[1]*0.923 + data[2]) / 2
    print("%.3f" % ans)
else:
    ans = (data[1] + data[2]) / 2 * 1.08
    print("%.3f" % ans)

