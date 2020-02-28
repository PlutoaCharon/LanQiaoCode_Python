n = int(input())
str = 'ABA'
if n == 1:
    print('A')
elif n == 2:
    print('ABA')
else:
    for i in range(3, n+1):
        str = str + chr((i + 64)) + str
    print(str)