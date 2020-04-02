while True:
    try:
        n = int(input())
        def rec(n):
            s = list(bin(n))[2:][::-1]
            for i in range(len(s)-1,-1,-1):
                if s[i] == '1':
                    if i == 0:
                        print('2(0)',end='')
                        return
                    elif i == 1:
                        print('2',end='')
                        if s[0] != '0':
                            print('+',end = '')
                    elif i == 2:
                        print('2(2)',end='')
                        if s[:2] != ['0','0']:
                            print('+',end='')
                    else:
                        print('2(',end='')
                        rec(i)
                        print(')',end='')
                        if s[:i] != ['0'for _ in range(i)]:
                            print('+',end='')
                else:
                    continue
        rec(n)
    except:
        break
