'''
问题描述
　　石子游戏的规则如下：
　　地上有n堆石子，每次操作可选取两堆石子（石子个数分别为x和y）并将它们合并，操作的得分记为(x+1)×(y+1)，对地上的石子堆进行操作直到只剩下一堆石子时停止游戏。
　　请问在整个游戏过程中操作的总得分的最大值是多少？
输入格式
　　输入数据的第一行为整数n，表示地上的石子堆数；第二行至第n+1行是每堆石子的个数。
输出格式
　　程序输出一行，为游戏总得分的最大值。
样例输入
10
5105
19400
27309
19892
27814
25129
19272
12517
25419
4053
样例输出
15212676150
'''
def solve(arr):
    ans = 0
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        tmp = (arr[-1] + 1) * (arr[-2] + 1)
        num = arr[-1] + arr[-2]
        arr.pop()  # 将最后相加的石子堆弹出
        arr.pop()  # 将最后相加的石子堆弹出
        arr.append(num)
        ans += tmp
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    ans = solve(arr)
    print(ans)
