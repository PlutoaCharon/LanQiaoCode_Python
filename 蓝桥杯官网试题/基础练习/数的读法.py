n = input()

pin_yin = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu',
           '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
pin_yin_2 = {0: '', 1: '', 2: 'shi', 3: 'bai', 4: 'qian', 5: 'wan', 6: 'shi',
             7: 'bai', 8: 'qian', 9: 'yi', 10: 'shi'}
n = n + ' '
#
l = len(n) - 1
for i in range(l):
    j = int(n[i])
    if j != 0:  # 不为0时的读法
        if (l - i == 2 or l - i == 6 or l - i == 10) and j == 1:
            # 在十位，十万位，十亿位置且位于开头的1不读
            # 例子：
            # 1111111111 会读出 yi shi yi yi yi qian yi bai yi shi yi wan yi qian yi bai yi shi yi
            # 111111 会读出 yi shi yi wan yi qian yi bai yi shi yi
            # 11 会读出 yi shi yi
            # 加上此约束后，则不会读出开头的 yi
            if i != 0:  # 第一个1不输出1， 若不添加此条件，12会读出 yi shi er
                print(pin_yin['1'], end=' ')
            print(pin_yin_2[2], end=' ')
            continue
        print(pin_yin[n[i]], end=' ')
        print(pin_yin_2[l - i], end=' ')
    else:  # 处理0的读法问题
        if l - i == 5 or l - i == 9:  # 如果此0是在万位或亿位，则读出万或亿
            print(pin_yin_2[l - i], end=' ')
        if n[i + 1] == '0' or i == l - 1:  # 如果后一位仍然为0，或者，当前是最后一位，则不读此0
            continue
        print(pin_yin['0'], end=' ')  # 否则才读出这个零
