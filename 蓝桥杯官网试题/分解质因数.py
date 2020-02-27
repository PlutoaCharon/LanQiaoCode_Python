# 方法1

# def solve(num):
#     list = []
#     tmp = 2
#     if num == tmp:
#         print(num,'=', num, sep='')
#     else:
#         print(num,'=', sep='', end='')
#         while num >= tmp:
#             if num % tmp ==0:
#                 list.append(tmp)
#                 num = num / tmp
#             else:
#                 tmp += 1
#         for i in range(len(list)-1):
#             print(list[i], '*', sep='', end='')
#         print(list[-1])
# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     for i in range(a, b+1):
#         solve(i)
def solve(res, n, result):
    for i in range(2, n+1):
        if n % i ==0:
            res += str(i)
            n = n // i
            if n == 1:
                return res
            elif n in result.keys():
                res += '*'
                res += result[n]
                return res
            else:
                res += '*'
                return solve(res, n, result)
        else:
            continue

if __name__ == '__main__':
    a, b = map(int, input().split()) # 输入两个整数
    result = {}   # result存放值与其分解质因数的对应关系
    # {3: '3', 4: '2*2', 5: '5', 6: '2*3', 7: '7', 8: '2*2*2', 9: '3*3', 10: '2*5'}

    for i in range(a, b+1):
        res = ''  # 存放各个因数
        result[i] = solve(res, i, result)

    # 输出
    for k, v in result.items():
        s = str(k)+ '='+ str(v)
        print(s)
