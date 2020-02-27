'''
输入:
4
4
1 3 1 3
3
3 3 2
5
2 3 3 4 2
3
1 1 2
输出:
2
1
2
0
'''
T = int(input())
num = 0

for i in range(T):
    n = int(input())
    length = list(map(int, input().split()))
    length.sort()
    second = length[n-2]
    print(min(n-2, second-1))
