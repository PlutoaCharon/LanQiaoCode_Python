'''
3
  A
 BBB
CCCCC
'''
n = int(input())
for i in range(1, n+1):
    space = (n - i) * ' '
    ch = chr(i+64) * (2*i - 1)
    print(space+ch)
