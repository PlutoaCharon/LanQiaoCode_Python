def Sine_An(n, k):
    if n == k: # 返回值
        return
    print('sin(%d' % (n+1), end='')

    if n + 1 != k: # 当n小于输入的值,即后面还有式子
        if n % 2 == 1: # 如果n是奇数 输出+号
            print('+', end='')
        else:         # 如果n是偶数 输出-号
            print('-', end='')
    else:          # 如果后面没有式子输出右括号
        print(')', end='')

    Sine_An(n+1, k)

def Sine_Sn(n):
    k = t = 1

    if n == 0:
        return

    for i in range(n-1): # 补全左边括号
        print('(', end='')

    while n != 0:
        Sine_An(0,k)
        for i in range(t-1):
            print(')', end='') # 补全An的右括号
        print('+%d' % n, end='')
        if n !=1:
            print(')', end='')

        k+=1
        t+=1
        n-=1
if __name__ == '__main__':
    n = int(input())
    Sine_Sn(n)
