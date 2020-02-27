str = list(input())
# a=97 z=122 A=65 Z=90
for i in range(len(str)):
    if 65 <= ord(str[i]) <=122:
        if str[i] == 'z':
            str[i] = 'a'
        elif str[i] == 'Z':
            str[i] = 'A'
        else:
            str[i] = chr(ord(str[i])+1)
    else:
        continue
for i in str:
    print(i, end='')