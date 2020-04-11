ans = 0
num1 = 0
s = input()
h = input()
ls = len(s)
lh = len(h)
for i in s:
    num1 += ord(i)
for i in range(lh - ls + 1):
    num2 = 0
    for j in range(i, i + ls):
        num2 += ord(h[j])
    if num1 == num2:
        ans += 1
print(ans)