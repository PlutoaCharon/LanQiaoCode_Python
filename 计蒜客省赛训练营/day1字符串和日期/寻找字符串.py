'''
输入:
ossosso
osso

输出:
2
'''
str = input()
target = input()
ans = 0
len_t = len(target)
for i in range(len(str)):
    if str[i] == target[0]:
        if str[i:i+len_t-1] == target[0:len_t-1]:
            ans += 1
print(ans)