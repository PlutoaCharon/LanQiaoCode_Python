str = input()
str = str[::-1]
ans = ""
cnt = 0
for i in range(len(str)):
    if cnt == 3:
        ans = ans + ","
        cnt = 0
    cnt += 1
    ans = ans + str[i]
ans = ans[::-1]
print(ans)



