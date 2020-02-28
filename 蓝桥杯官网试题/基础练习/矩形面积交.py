list1 = list(map(float, input().split()))
list2 = list(map(float, input().split()))

x1 = max(min(list1[0], list1[2]), min(list2[0], list2[2]))
x2 = min(max(list1[0], list1[2]), max(list2[0], list2[2]))
y1 = max(min(list1[1], list1[3]), min(list2[1], list2[3]))
y2 = min(max(list1[1], list1[3]), max(list2[1], list2[3]))

if x1 < x2 and y1 < y2:
    area = (x2 - x1)*(y2 - y1)
    print('%.2f' % area)
else:
    print('%.2f' % 0.00)
