'''
# python 大数
a = int(input())
b = int(input())
print(a+b)
'''

# 方法2:
def change_length(str_num, l):
    # 添加前导0
    str_num = '0' * (l -len(str_num)) + str_num
    return str_num

if __name__ == '__main__':
    num1 = input()
    num2 = input()
    # 修改长度
    if len(num1) > len(num2):
        num2 = change_length(num2, len(num1))
    elif len(num1) < len(num2):
        num1 = change_length(num1, len(num2))
    # 结果最多比最长的num长1个单位
    ans_num = [0 for _ in range(len(num1) + 1)]
    # 进位
    k = 0

    for i in range(len(num1)):
        val = k + int(num1[len(num1) - i - 1]) + int(num2[len(num2) - i - 1])
        ans_num[len(num1) - i] = val % 10
        k = 0
        if  val >= 10:
            k = int(val // 10)

    if k != 0:
        ans_num[0] = k
        for i in range(len(ans_num) - 1):
            print(ans_num[i], end='')
        print(ans_num[-1])
    else:
        for i in range(len(ans_num) - 2):
            print(ans_num[i+1], end='')
        print(ans_num[-1])












