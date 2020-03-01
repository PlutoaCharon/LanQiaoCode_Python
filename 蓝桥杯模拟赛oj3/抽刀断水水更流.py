nums = [3,5,7,11,13,19,23,29,31,37,41,53,59,61,67,71,97,101,127,197,211,431]
ans = [] #存放所有答案

for i in range(1<<22): # 2^22-1种情况(这里是取0或者取22个数的全部可能情况)
    cnt = 0 # 计数 控制取数不超过12
    res = 0 # 结果
    tmp = i
    for j in range(22): # 查看22位中都有哪一位放了数字,即是1
        if (tmp >> j) & 1: # 如果第j位是1,则符合
            cnt += 1
            res += nums[j]
        if cnt <= 12:    # 不超过12位
            ans.append(res)
ans = set(ans)         # 使用集合的特性,去重
cnt = 1695
print(ans)
print(cnt - len(ans))