def brace_match(str):
    stack = []
    for ch in str:
        if ch in {'(', '{', '['}:
            stack.append(ch)
        elif len(stack) == 0:
            return False
        elif brace_arr[stack[-1]] == ch:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True

if __name__ == '__main__':
    str = input()
    brace_arr = {'(':')', '{':'}', '[':']'}
    if brace_match(str):
        print('Yes')

