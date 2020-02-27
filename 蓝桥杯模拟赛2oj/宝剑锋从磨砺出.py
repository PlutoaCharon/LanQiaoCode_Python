n,k = map(int, input().split())
ans = 0
list1 = []
list2 = []
for i in range(n):
    a,b = map(int, input().split())
    list1.append(a)
    list2.append(b)
list1 = sorted(list1)
list2 = sorted(list2)
while list2 and list2[-1] > list1[-1] and k > 0:
    k -= list2[-1]
    list2.pop()
    ans += 1
if k > 0:
    ans += k // list1[-1] + 1
print(ans)
