def is_ans(num, list):
    for i in range(len(list)):
        if num == list[i]:
            print(i+1)
            break
    if num not in list:
        print(-1)


if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().split()))
    num = int(input())
    is_ans(num, list)
