def solve(list):
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                if (list[i] + list[j] + list[k]) % 10 == 0:
                    num1 = list[i]
                    num2 = list[j]
                    num3 = list[k]
                    list.remove(num1)
                    list.remove(num2)
                    list.remove(num3)
                    if (list[0] + list[1]) % 10 == 0:
                        str1 = "so cool!"
                        return str1
                    else:
                        return (list[0] + list[1]) % 10

                else:
                    continue
    else:
        str2 = "so sad!"
        return str2

if __name__ == '__main__':

    str = input()
    str = str.replace('A','1')
    str = str.replace('S','10')
    str = str.replace('K','10')
    str = str.replace('Q','10')
    str = str.replace('J','10')
    list = list(str.split())
    for i in range(len(list)):
        list[i] = int(list[i])

    ans = solve(list=list)
    print(ans)