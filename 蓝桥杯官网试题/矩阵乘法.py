def solve(N, rect1, rect_ans):
    rect2 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):  # 行
        for j in range(N):  # 列
            for n in range(N):
                rect2[i][j] += rect1[i][n] * rect_ans[n][j]
    return rect2

if __name__ == '__main__':
    N, M =map(int, input().split())     # 输入数据
    rect1 = [[] for _ in range(N)]       # 定义矩阵

    for i in range(N):
        arr = input().split()
        for j in range(N):
            rect1[i].append(int(arr[j])) # 输入数据

    if M > 0:
        # 矩阵的幂
        rect_ans = rect1
        for i in range(M-1):
            rect_ans = solve(N, rect1, rect_ans)
    else:
        # 幂等于0时,输出单位矩阵
        rect_ans = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            rect_ans[i][i] = 1

    # 格式化输出
    for i in range(N):
        for j in range(N):
            print(rect_ans[i][j], end=' ')
        print()
