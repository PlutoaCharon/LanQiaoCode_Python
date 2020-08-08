'''
问题描述
　　给定两个字符串，寻找这两个字串之间的最长公共子序列。
输入格式
　　输入两行，分别包含一个字符串，仅含有小写字母。
输出格式
　　最长公共子序列的长度。
样例输入
abcdgh
aedfhb
样例输出
3
样例说明
　　最长公共子序列为a，d，h。
数据规模和约定
　　字串长度1~1000。
'''


def lcs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    arr = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

    for i in range(l2 + 1):
        for j in range(l1 + 1):
            if i == 0 or j == 0:  # arr[0][j] 与 arr[i][0]全部置为0
                arr[i][j] = 0
            elif i > 0 and j > 0 and str2[i - 1] == str1[j - 1]:  # 如果有相等的字符, 则加1
                arr[i][j] = 1 + arr[i - 1][j - 1]
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])

    return arr


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    ansList = lcs(str1, str2)
    print(ansList[-1][-1])
