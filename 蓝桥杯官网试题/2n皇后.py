while True:
    try:
        #我们先白皇后，再黑皇后
        n = int(input())   #n是一开始的黑白皇后个数
        s = []             #存放原始的0,1位置
        result = []
        temp_W = [None for x in range(n)]  #临时放一下白皇后
        temp_B = [None for x in range(n)]  #临时放一下黑皇后
        for i in range(n):
           s.append(input().split())      #输入0, 1位置
        def valid_W(temp_W,row):    #判断当前的位置上放白皇后是否合法
            if s[row][temp_W[row]] == '1':   #判断这个位置能否放置皇后
                for i in range(row):
                    #下面这个判断条件是：判断对角线，判断是否是白皇后自己的列
                    if abs(temp_W[i] - temp_W[row]) == abs(i-row) or temp_W[i] == temp_W[row]:
                        return False
                return True

        def valid_B(temp_B,row,temp_W):    #判断当前的位置放黑皇后是否合法
            if s[row][temp_B[row]] == '1' and temp_B[row] != temp_W[row]:   #判断这个位置能否放置皇后
                for i in range(row):
                    #判断是否对角线，是否是自己的列，判断这个位置有没有先放上白皇后
                    if abs(temp_B[i] - temp_B[row]) == abs(i-row) or temp_B[i] == temp_B[row]:
                        return False
                return True

        def dfs_W(temp_W,row):   #temp记录当前所有合法的皇后的位置，row是继续往下一行里面放皇后
            if row == n:   #当前进行到n,表示找到了白皇后的一种排列方式，跳出递归
                dfs_B(temp_B,0)    #白皇后排好之后跳到排列黑皇后
            else:
                for col in range(n):   #col是列，就是要遍历这一行的所有列，看在某个位置上是否合法
                    temp_W[row] = col
                    if valid_W(temp_W,row):
                        dfs_W(temp_W,row+1)

        def dfs_B(temp_B, row):   #temp记录当前所有合法的皇后的位置，row是继续往下一行里面放皇后
            if row == n:   #当前进行到n,表示找到了n皇后的一种排列方式，跳出递归
                result.append(temp_B[:])#将找到的黑皇后排列方式存储到result里面
                return
            else:
                for col in range(n):   #col是列，就是要遍历这一行的所有列，看在某个位置上是否合法
                    temp_B[row] = col
                    if valid_B(temp_B,row,temp_W):
                        dfs_B(temp_B,row+1)

        dfs_W(temp_W,0)
        print(result)
        print(len(result))
    except:
        break
