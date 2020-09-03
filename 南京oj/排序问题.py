'''
按照年份排序

输入:
4
Boston 1963
Boston 1959
Philly 1947
New York 1970

输出:
[['Philly', '1947'], ['Boston', '1959'], ['Boston', '1963'], ['New', 'York', '1970']]
'''


def take_year(arr):
    return arr[-1]


n = int(input())
nba_queue = []
for i in range(n):
    nba_queue.append(input().split())
nba_queue = sorted(nba_queue, key=lambda x: x[-1])
nba_queue = sorted(nba_queue, key=take_year)
print(nba_queue)
