n = int(input())

for line in range(n):
    num = input()
    ans = format(int(num, 16), 'o')
    print(ans)