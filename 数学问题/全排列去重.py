def backtrack(nums, tmp):
    if not nums:
        res.append(tmp)
        return
    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])

if __name__ == '__main__':
    res = []
    n = int(input())
    # listq = list(map(int, input().split()))
    listq = list(map(str, input()))
    backtrack(listq, [])
    print(res)
    print(len(res))
    ans = list(set([tuple(_) for _ in res]))
    print(ans)
    print(len(ans))