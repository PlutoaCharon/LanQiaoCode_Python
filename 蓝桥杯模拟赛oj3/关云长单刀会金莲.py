'''
我们通过枚举每一个名著的开始阅读时间，然后判断这种可能方案，满不满足要求。也就是每一本名著读书的那天，不能读其他的。
我们可以用一个变量 vis，记录每一天是否已经读过了
'''

def is_True(a,b,c,d):
    vis = [0 for _ in range(32)]
    for i in range(4):
        vis[a+i] = 1
    for i in range(3):
        if vis[b+i] != 1:
            vis[b+i] = 1
        else:
            return False
    for i in range(5):
        if vis[c + i] != 1:
            vis[c + i] = 1
        else:
            return False
    for i in range(3):
        if vis[d + i] != 1:
            vis[d + i] = 1
        else:
            return False
    return True
if __name__ == '__main__':
    # a = 《水浒传》 4天
    # b = 《西游记》 3天
    # c = 《三国演义》 5天
    # d = 《红楼梦》 3天
    ans = 0
    for a in range(1, 29): # 第28天为最晚读书日期
        for b in range(1, 30):# 第29天为最晚读书日期
            for c in range(1, 28):# 第27天为最晚读书日期
                for d in range(1, 30):# 第28天为最晚读书日期
                    if is_True(a,b,c,d):
                        ans += 1

    print(ans)