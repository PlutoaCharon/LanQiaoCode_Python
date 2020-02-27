ans = 0
for a in range(1,10):
    for b in range(1, 10):
        if a!=b:
            for c in range(1, 10):
                if c!=a and c!=b:
                    for d in range(1, 10):
                        if d!=a and d!=b and d!=c:
                            for e in range(1, 10):
                                if e!=a and e!=b and e!=c and e!=d:
                                    if int(str(a)+str(b)) * int(str(c)+str(d)+str(e)) == int(str(a)+str(d)+str(b)) * int(str(c)+str(e)):
                                        str1 = str(a)+str(b)+'*'+ str(c)+str(d)+str(e)+ "=" + str(a)+str(d)+str(b)+ '*'+ str(c)+str(e)
                                        ans += 1
                                        print(ans)
                                        print(str1)
print("正确答案:", ans)