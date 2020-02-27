'''
2020年，这个年份很特别，2020从中间分成两个整数，大小形状完全一样。

小明对形如2020的数字很感兴趣(不包括前导零)，在1到1200中这样的数字包括11、22、33、44、55、66、77、88、99、1010、1111共11个，他们的和是2616

请问，在1到n中，所有这样的数的和是多少？
'''
n = int(input())
sum = 0
for i in range(1, n+1):
    if int(len(str(i))) % 2 == 0:
        if i <= 99:
            left = str(i)[0]
            right = str(i)[1]
            if left == right:
                sum += i
            else:
                continue
        else:
            half_len = len(str(i)) // 2
            left = str(i)[0:half_len]
            right = str(i)[half_len:]
            if left == right:
                sum += i
            else:
                continue
print(sum)

