ans = 0
for i in range(1, 141517):
    tmp = 0

    for j in str(i):
        tmp += int(j)

    if "2" not in str(i) and "4" not in str(i):
        if len(str(pow(tmp, 1 / 2))) == 3 or len(str(pow(tmp, 1 / 3))) == 3:
            ans += 1
            print(i)
print(ans)

'''
a=str(input())
b=str(input())
a1=[0]*26
b1=[0]*26
for i in range(len(a)):
    a1[ord(a[i])-97]+=1
    b1[ord(b[i])-97]+=1
sum=0
flag=0
for i in range(26):
    if a1[i]!=b1[i]:
        break
    if i==25:
        flag=1
if flag==1:
    sum+=1
j=0
for i in range(len(a),len(b)):
    flag=0
    b1[ord(b[j])-97]-=1
    j+=1
    b1[ord(b[i])-97]+=1
    for i in range(26):
        if a1[i]!=b1[i]:
            break
        if i==25:
            flag=1
    if flag==1:
        sum+=1
print(sum)
'''