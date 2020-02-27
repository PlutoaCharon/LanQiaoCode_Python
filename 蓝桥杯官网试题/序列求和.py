'''
# 超时1s
tmp = 1
n = int(input())
if n == 1:
    print(1)
else:
    for val in range(2, n+1):
        num = tmp + val
        tmp = num
    print(num)
'''

# 等差数列

def sum():
    n = int(input())
    return n*(1+n)/2
s = int(sum())
print(s)
    
