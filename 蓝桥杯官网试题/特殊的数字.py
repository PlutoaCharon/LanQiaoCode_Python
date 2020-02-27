# def is_ans(num):
#     num_sum = pow(int(str(num)[0]), 3) + pow(int(str(num)[1]), 3) + pow(int(str(num)[2]), 3)
#     if num == num_sum:
#         return True
#
# for ans in range(100, 1000):
#     if is_ans(ans):
#         print(ans)

def is_ans(num):
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    if num == pow(a, 3) + pow(b, 3) + pow(c, 3):
        return True

for ans in range(100, 1000):
    if is_ans(ans):
        print(ans)