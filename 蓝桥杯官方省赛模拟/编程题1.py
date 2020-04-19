ans = ""
strq = list(input())
for i in range(len(strq)):
    if 97 <= ord(strq[i]) <= 119:
        strq[i] = chr(ord(strq[i]) + 3)
    else:
        strq[i] = chr(ord(strq[i]) - 120 + 97)
for i in range(len(strq)):
    ans += strq[i]
print(ans)
