def is_pingfang(n):
    for i in range(2, 32):
        if pow(i, 2) == n:
            return True
        else:
            continue
def is_lifang(n):
    for i in range(2, 10):
        if pow(i, 3) == n:
            return True
        else:
            continue

def is_sifang(n):
    for i in range(2, 6):
        if pow(i, 4) == n:
            return True
        else:
            continue

def is_huiwen(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
def is_sanjiao(n):
    for i in range(1, 46):
        n -= i
        if n == 0:
            return True
        else:
            continue
def is_zhishu(n):
    flag = True
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            flag = False
            break
    return flag



if __name__ == '__main__':
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            for g in range(1, 10):
                                for h in range(1, 10):
                                    for i in range(1, 10):
                                        if is_lifang(int(str(a)+str(b)+str(c))) and is_zhishu(int(str(d) + str(e) + str(f))) and is_pingfang(int(str(g) + str(h) + str(i))) and is_sanjiao(int(str(a) + str(d) + str(g))) and is_sifang(int(str(b) + str(e) + str(h))) and is_huiwen(int(str(c) + str(f) + str(i))):
                                            print("正确答案:")
                                            print(a, b, c, d, e, f, g, h, i)
                                            break
                                        else:
                                            continue
