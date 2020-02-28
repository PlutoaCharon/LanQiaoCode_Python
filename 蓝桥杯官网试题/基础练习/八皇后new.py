class Solution(object):
    def solveNQueens(self, n):

        k = 0 # 表示准备放置的第k+1个棋子

        ans, q = [], [None] * n # q表示一位数组形式的答案棋盘

        def dfs(k, n):
            if k == n: # k=n 时表示棋子全部放置完成,输出棋盘
                tmp = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        s += "Q" if q[i] == j else '.'
                    tmp.append(s)
                ans.append(tmp)
            else:
                for j in range(n):
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k + 1, n)

        dfs(k, n)
        return ans, len(ans)

    def place(self, k, j, q):
        for i in range(k):
            # 当q[i] == j时表示在同一列
            # abs(q[i] - j) == abs(i - k) 表示在同一对角
            if q[i] == j or abs(q[i] - j) == abs(i - k):
                return False
        return True

if __name__ == '__main__':
    solu = Solution()
    solu.solveNQueens(4)
    # print(solu.solveNQueens(4))