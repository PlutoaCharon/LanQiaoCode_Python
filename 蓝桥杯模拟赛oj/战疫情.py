sum = 0
for x in range(21001):
    for y in range(21001):
        if 20000 <= x+y <= 21000 and ((2*x) + (100*y)) == 50000:
            sum += 1
            print(x, y, sum)
        else:
            continue
