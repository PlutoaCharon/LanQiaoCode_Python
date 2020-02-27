def queen(A, cur=0):

    # 递归回溯思想解决n皇后问题
    if cur == len(A): # 所有的皇后都正确放置完毕，输出每个皇后所在的位置
        tmp = []
        for i in range(n):
            s = ''
            for j in range(n):
                s+='Q' if A[i] == j else '.'
            tmp.append(s)
        ans.append(tmp)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur): # 检测本次所放皇后的位置是否在同行同列或同一对角线上
            if A[row] == col or abs(col - A[row]) == cur - row: # 是的话，该位置不能放，向上回溯
                flag = False
                break
        if flag: # 否的话，继续放下一个皇后
            queen(A, cur+1)


n = int(input())
ans = []
queen([None] * n)
print(ans)


