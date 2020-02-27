def is_ans(n, list):
    list = sorted(list)
    max = list[-1]
    min = list[0]
    sum = 0
    for i in list:
        sum += i
    print(max)
    print(min)
    print(sum)

if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().split()))
    is_ans(n, list)


'''
n = int(input())

arr = input().split()

print(max(int(arr[i]) for i in range(n))) # 最大值
print(min(int(arr[i]) for i in range(n))) # 最小值
print(sum(int(arr[i]) for i in range(n))) # 求和
'''