'''
描述
求所有 2 到 n 的整数中，因数个数第k少的数因数个数是多少。

输入
第一行两个正整数 n,k即题目描述中的 n,k

输出
输出仅一行，即因数个数第 k少的数因数个数。
'''
'''
# 方法1
def get_num_factors(num):
    tmp = 1
    ll = 0
    if num == tmp:
        return num
    else:
        while num >= tmp:
            k = num % tmp
            if k == 0:
                ll += 1
                tmp += 1
            else:
                tmp += 1
    return ll

if __name__ == '__main__':
    n,k = map(int, input().split())
    list = []
    for i in range(2, n+1):
        list.append(get_num_factors(i))
    list = sorted(list)
    print(list[k-1])
'''
# 方法二
'''
我们利用素数筛选的原理，两重循环，第一重 i : 2 到 n，第二重，j = 2 * i，到 n（间隔 i ），也就是，当我们找到 i，那么 i 的倍数的因子个数 + 1，因为 i 是所有 i 的倍数的因子。
'''

if __name__ == '__main__':
    n, k = map(int, input().split())
    qList = [2 for i in range(n + 1)]  # 初始因数都为2 (1和本身)

    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            qList[j] += 1  # 所有i倍数的因数加一

    ansList = sorted(qList)[2:]  # 从2-n开始, 所以取出0,1
    print(ansList[k - 1])  # 因为列表从0开始计数
