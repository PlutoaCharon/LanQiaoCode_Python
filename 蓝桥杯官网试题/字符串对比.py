def solve(str1, str2):
    if len(str1) != len(str2):
        return 1
    else:
        if str1 == str2:
            return 2
        elif str1.lower() != str2.lower():
            return 4
        return 3
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(solve(str1, str2))
