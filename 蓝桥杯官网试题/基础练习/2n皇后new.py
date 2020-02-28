def correctWhite(tmpWhite, row):
    if arr[row][tmpWhite[row]] == 1: # tmpWhite[row]表示第几列 ,如果此位置是1, 则表示可以放置
        for i in range(row):        # 判断条件为不在同一列,和不在同一对角线上
            if abs(tmpWhite[i] - tmpWhite[row]) == abs(i - row) or tmpWhite[i] == tmpWhite[row]:
                return False
        return True

def correctBlack(tmpBlack, row, tmpWhite):
    if arr[row][tmpBlack[row]] == 1 and tmpBlack[row] != tmpWhite[row]: # tmpBlack[row]表示第几列 ,如果此位置是1和此位置不和白皇后冲突, 则表示可以放置
        for i in range(row):            # 判断条件为不在同一列,和不在同一对角线上
            if abs(tmpBlack[i] - tmpBlack[row]) == abs(i - row) or tmpBlack[i] == tmpBlack[row]:
                return False
        return True

def dfs_Black(tmpBlack, row):
    if row == n: # 此时黑皇后和白皇后的位置全部确定, 将结果输入到ans列表中
        ans.append(tmpBlack[:])
        return    # 退出递归
    else:
        for col in range(n):
            tmpBlack[row] = col
            if correctBlack(tmpBlack, row, tmpWhite): # 如果位置合法
                dfs_Black(tmpBlack, row + 1)         # 开始下一个黑皇后的放置


def dfs_White(tmpWhite, row):
    if row == n:   # 如果此时确定了白皇后的全部位置,开始放置黑皇后
        dfs_Black(tmpBlack,0)
    else:
        for col in range(n):    # 从第一个白皇后开始放置
            tmpWhite[row] = col
            if correctWhite(tmpWhite, row): # 如果位置可以放置
                dfs_White(tmpWhite, row+1)  # 开始放置下一个白皇后
if __name__ == '__main__':

    # 输入n与棋盘, 其中棋盘用二维数组表示
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 设置临时存放黑白皇后的棋盘
    tmpWhite = [None for _ in range(n)]
    tmpBlack = [None for _ in range(n)]
    ans = []
    # 先从白皇后放置开始
    dfs_White(tmpWhite, 0)
    print(len(ans))
