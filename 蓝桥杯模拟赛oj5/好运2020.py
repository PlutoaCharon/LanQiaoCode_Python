'''

'''

def solve(num):
    list = []
    tmp = 2
    if num == tmp:
        list.append(num)
        return len(set(list))
    else:
        while num >= tmp:
            if num % tmp ==0:
                list.append(tmp)
                num = num / tmp
            else:
                tmp += 1
        return len(set(list))
if __name__ == '__main__':
    cnt = 0
    for i in range(1, 2021):
        if solve(i) != 4:
            cnt += 1
    print(cnt)