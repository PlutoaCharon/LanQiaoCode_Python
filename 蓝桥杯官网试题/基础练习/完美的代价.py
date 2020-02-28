'''

# 方法1
n = int(input())

pal = list(input())

count = flag = 0  # count计数，flag判断是否已经有一个单独的奇个数的字符了

m = n - 1

for i in range(m):  # 从头遍历到倒数第二个字符
    for k in range(m, i - 1, -1):  # 从后面往前一直到i寻找和pal[i]相同的pal[k]
        if k == i:  # 如果找不到相同的
            if n % 2 == 0 or flag == 1:  # impossible的两种情况
                print('Impossible')
                exit()
            flag = 1
            count += int(n / 2) - i
        elif pal[k] == pal[i]:
            for j in range(k, m):  # 找到相同的，进行交换
                pal[j], pal[j + 1] = pal[j + 1], pal[j]
                count += 1  # 计数器加1
            m -= 1  # 最后拍好序的不在进行比较
            break

print(count)
#
'''

# 方法2
def is_pal(n, s):
    temp = set()
    if n % 2 == 0:
        for i in range(26):
            if s.count(chr(ord('a') + i)) % 2 != 0:
                print('Impossible') # 如果字符串字符为偶数,但是存在不成对字符
                return False
        else:
            return True
    else:
        for i in range(26):
            if s.count(chr(ord('a') + i)) % 2 != 0:
                temp.add(chr(ord('a') + i))
            if len(temp) > 1:
                print('Impossible')  # 如果字符串字符为奇数,但是存在不成对字符超过一个
                return False
        else:
            return True

def count_step(n, s, s1):
    global ans
    for i in range(n // 2):
        if s[i:].count(s[i]) != 1:
            temp = s1[:n - i].index(s[i])
            s1.pop(temp)
            ans += temp
            s = s1[::-1]
        else:
            ans += n // 2 - i
            s[i] = None # 将此奇数移动到中间后清除
            s1 = s[::-1]
    return ans

if __name__ == '__main__':
    n = int(input()) # 字符串的长度
    s = list(input()) # 输入字符串
    s1 = s[::-1]
    ans = 0

    if is_pal(n, s):    # 如果是回文数 计算挪动的步数
        print(count_step(n, s, s1))

