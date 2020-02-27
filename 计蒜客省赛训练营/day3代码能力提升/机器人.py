'''
蒜头君收到了一份礼物，是一个最新版的机器人。这个机器人有 4 种指令：
forward x，前进x米。
back x，先向后转，然后前进x米。
left x，先向左转，然后前进x米。
right x，先向右转，然后前进x米。
现在把机器人放在坐标轴原点，起始朝向为x轴正方向。经过一系列指令以后，你能告诉蒜头君机器人的坐标位置吗。坐标轴上一个单位长度表示1米。

样例输入:
10
back -9
left 3
left 8
back 15
right 10
right -7
right -3
left 11
right 17
left 3

样例输出:
9 -7

'''
n = int(input())

dx = [0,-1, 0, 1]  #上左下右
dy = [1, 0,-1, 0]  #上左下右

now_dir = 3

nowx = 0
nowy = 0
for i in range(n):
    dir, x = map(str, input().split())
    x = int(x)
    if dir[0] == 'b':
        now_dir = (now_dir+2) % 4  # 向后
    elif dir[0] == 'l':
        now_dir = (now_dir+1) % 4  # 向左
    elif dir[0] == 'r':
        now_dir = (now_dir+3) % 4  # 向右
    nowx += dx[now_dir] * x
    nowy += dy[now_dir] * x

print(nowx, nowy)