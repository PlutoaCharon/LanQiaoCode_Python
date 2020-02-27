def triangles(num):
    n = [1]
    while num > 0:
        for i in range(len(n)):
            print(n[i], end=' ') # 将列表转为要求的格式
        n = [1] + [n[i] + n[i+1] for i in range(len(n) - 1)] + [1]
        num -= 1
        print()                  # 换行
if __name__ == '__main__':
    n = int(input())
    triangles(n)