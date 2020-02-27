'''
特殊的三角形

输入:9
输出:
        1
       121
      12321
     1234321
    123454321
   12345654321
  1234567654321
 123456787654321
12345678987654321
输入:C
输出:
  A
 ABA
ABCBA
'''
n = input()
if ord(n) < 65:
    n = int(n)
    for i in range(1, n+1):
        for j in range(1, n + 1 - i):
            print(' ', end='')
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i , 1, -1):
            print(j-1, end='')
        print()
else:
    ch = ord(n)
    for i in range(65, ch + 1):
        for j in range(1, ch - i + 1):
            print(' ', end='')
        for j in range(65, i + 1):
            print(chr(j), end='')
        for j in range(i, 65, -1):
            print(chr(j - 1), end='')
        print()


