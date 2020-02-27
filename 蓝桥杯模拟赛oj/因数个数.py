'''
描述
求所有 2 到 n 的整数中，因数个数第k少的数因数个数是多少。

输入
第一行两个正整数 n,k即题目描述中的 n,k

输出
输出仅一行，即因数个数第 k少的数因数个数。
'''

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
    list = sorted(list, n-1)
    print(list[k-1])


