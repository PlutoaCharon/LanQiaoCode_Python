'''
问题描述
　　对于给定整数数组a[],寻找其中最大值，并返回下标。
输入格式
　　整数数组a[],数组元素个数小于1等于100。输出数据分作两行：第一行只有一个数，表示数组元素个数；第二行为数组的各个元素。
输出格式
　　输出最大值，及其下标
'''
n = int(input())
list1 = list(map(int, input().split()))
max = max(list1)
num = list1.index(max)
print(max,num)