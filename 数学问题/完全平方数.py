'''
链接：https://ac.nowcoder.com/acm/contest/5203/C
来源：牛客网

题目描述
多次查询[l,r]范围内的完全平方数个数

定义整数x为完全平方数当且仅当可以找到整数y使得y*y=x

输入描述:
第一行一个数n表示查询次数
之后n行每行两个数l,r
输出描述:
对于每个查询，输出一个数表示答案

示例1
输入
5
1 3
1 4
2 4
4 4
1 1000000000
输出
1
2
1
1
31622
备注:
n <= 100000
0<= l <= r <= 1000000000
'''
import math

n = int(input())
for i in range(n):
    A = list(map(int, input().split()))
    isum = int()
    a = math.ceil(pow(A[0], 1 / 2))
    b = math.floor(pow(A[1], 1 / 2))
    isum = b - a + 1
    print(isum)
