strq = input()  # 输入数据
ans = ""
s = 0  # 当前字符串长度
while len(strq) >= s + 1:
    cnt = 1
    num = 1
    if s+1 == len(strq):
        ans += strq[-1] + "1"
        break
    else:
        if strq[s] == strq[s + 1]:
            ans += strq[s]
            for i in range(s, len(strq) - 1):
                if strq[i] == strq[i + 1]:
                    cnt += 1
                    num += 1
                else:
                    break
            ans += str(cnt)
            s += num
        else:
            ans += strq[s] + "1"
            s += num
print(ans)
