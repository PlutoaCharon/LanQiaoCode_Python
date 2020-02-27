'''
问题描述】

定义数字x的价值为其不同质因子的个数。

例如:数字20202020可以写成2020=2*2*5*101，其价值为3.

JM boy请你帮忙计算整数1到2020中，所有都不包含数字5的正整数的价值之和。
'''
def get_num_factors(num):
    list = []
    tmp = 2
    if num == tmp:
        list.append(tmp)
    else:
        while num >= tmp:
            k = num % tmp
            if k == 0:
                if tmp not in list: # 去重
                    list.append(tmp)
                    num = num / tmp
                else:
                    num = num / tmp
            else:
                tmp += 1
    len_list = int(len(list))
    return len_list

if __name__ == '__main__':
    sum = 0
    for i in range(1, 2021):
        if '5' not in str(i):
            sum += get_num_factors(i)
            # print(i)
        else:
            continue
    print(sum)

