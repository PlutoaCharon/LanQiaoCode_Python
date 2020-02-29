ans = 0
for i in range(0, 100000000):
    s = str(i)
    s = s.zfill(8)
    if '2' in s:
        if '4' in s and '9' in s and s.count('4') == s.count('9'):
            if int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])+int(s[5])+int(s[6])+int(s[7]) <= 52:
                ans += 1
                print(i)
            else:
                continue
        elif '4' not in s and '9' not in s:
            if int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])+int(s[5])+int(s[6])+int(s[7]) <= 52:
                ans += 1
                print(i)
        else:
            continue
    else:
        continue
print(ans)