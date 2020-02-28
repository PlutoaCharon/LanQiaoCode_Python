n=int(input())
f1=f2=f3=1
if n == 1 or n == 2:
    print(1)
elif n > 2:
    for i in range(3,n+1):
        f3 = (f1 + f2) % 10007
        f1 = f2
        f2 = f3
    print(f3)
