'''
问题描述
　　Torry从小喜爱数学。一天，老师告诉他，像2、3、5、7……这样的数叫做质数。Torry突然想到一个问题，前10、100、1000、10000……个质数的乘积是多少呢？他把这个问题告诉老师。老师愣住了，一时回答不出来。于是Torry求助于会编程的你，请你算出前n个质数的乘积。不过，考虑到你才接触编程不久，Torry只要你算出这个数模上50000的值。
输入格式
　　仅包含一个正整数n，其中n<=100000。
输出格式
　　输出一行，即前n个质数的乘积模50000的值。
样例输入
1
样例输出
2
'''

'''
思路:
一个质数肯定不会被小于它的质数除尽
'''


def is_prime(num):
    for i in tmp:  # 遍历质数数组
        if num % i == 0:
            return False
    tmp.append(num)
    return True


if __name__ == '__main__':
    i = 3  # 如果n大于2, 从数字3开始遍历
    ans = 2  # 默认填入第一个质数
    tmp = [2]  # 质数数组
    n = int(input())
    while True:
        if len(tmp) >= n:
            break
        if is_prime(i):
            ans *= i
        i += 1
    print(ans % 50000)
