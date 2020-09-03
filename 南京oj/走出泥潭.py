row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col):
        if arr[i][j] == 1:
            if i == row - 1 and j == col - 1:
                print('(%d,%d)' % (i + 1, j + 1), end='')
            else:
                print('(%d,%d)' % (i + 1, j + 1), end='>')
