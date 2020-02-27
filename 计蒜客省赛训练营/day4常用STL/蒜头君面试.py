'''
蒜头君来蒜厂面试的时候，曾经遇到这样一个面试题：
给定 n 个整数，求里面出现次数最多的数，如果有多个重复出现的数，求出值最大的一个。当时可算是给蒜头君难住了。现在蒜头君来考考你。
输入格式
第一行输入一个整数n(1≤n≤100000)，接下来一行输入n个 int 范围内的整数。
输出格式
输出出现次数最多的数和出现的次数，中间用一个空格隔开，如果有多个重复出现的数，输出值最大的那个。
样例输入
10
9 10 27 4 9 10 3 1 2 6
样例输出
10 2
'''

from collections import Counter

n = int(input())
arr = list(input().split())

count = Counter(arr).most_common()
top = Counter(arr).most_common(1) # 取出现最多数的次数为top

ans = 0
for i in range(len(count)):
    tmp = 0
    if count[i][1] == top[0][1]:
        tmp = count[i][0]
    if int(tmp) > ans:
        ans = int(tmp)

print(ans, top[0][1])