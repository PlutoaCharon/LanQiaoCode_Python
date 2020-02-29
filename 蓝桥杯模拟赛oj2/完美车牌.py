ans = 0
for i in range(1, 1000000):
    i = str(i).zfill(6)
    if '2' in str(i) or '3' in str(i) or '4' in str(i) or '5' in str(i) or '7' in str(i):
        continue
    else:
        s = str(i)
        s1 = ''
        for i in range(6):
            if s[5-i] == '6':
                s1 += '9'
            elif s[5-i] == '9':
                s1 += '6'
            else:
                s1 += s[5-i]

        if s == s1:
            ans += 1
            print(s)
print(ans)
# 124 + 000000=
# 125