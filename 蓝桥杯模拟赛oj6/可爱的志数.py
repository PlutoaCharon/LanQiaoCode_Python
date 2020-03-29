ans = 0
for i in range(1, 200329):
    tmp = 0
    for j in range(1, i+1):
        if tmp > 3:
            break
        else:
            if i % j == 0:
               tmp += 1
    if tmp > 3:
        continue
    else:
        print(i)
        ans += 1
print(ans)