def f(n):
    x = 3
    #n为待转换的十进制数，x为机制，取值为2-16
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=n // x  # 商
        y=n % x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    ans = ''
    for i in b:
        ans += str(a[i])
    return ans

if __name__ == '__main__':
    ans = 0
    ans2 = 0
    for i in range(1, 2021):
        for j in range(1, 2021):
            a1 = f(i).count('1')
            a2 = f(i).count('2')
            b1 = f(j).count('1')
            b2 = f(j).count('2')
            if abs(int(a1)-int(a2)) == abs(int(b1)-int(b2)):
                ans += 1
            if i == j:
                ans2 += 1
    print(ans)
    print(ans2)