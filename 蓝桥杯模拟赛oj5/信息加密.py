ming = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mi = 'JKLMNOPQRSTUVWXYZABCDEFGHI'

s = input()
for i in s:
    print(ming[mi.index(i)], end='')
