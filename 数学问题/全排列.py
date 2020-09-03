# # 方法一
# '''
# 输入:
# 1 2 3
# 输出:
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
# '''
# import itertools
# n = list(map(int, input().split()))
# list = list(itertools.permutations(n))
# for i in range(len(list)):
#     print(list[i])
# 方法二
nums = [1, 2, 3]
res = []


def backtrack(nums, tmp):
    if not nums:
        res.append(tmp)
        return
    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])


backtrack(nums, [])
print(res)
