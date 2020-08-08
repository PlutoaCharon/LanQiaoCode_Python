s = "(()"
ans = 0  # 最大合法长度(返回值)
stack = [-1, ]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
for i, ch in enumerate(s):
    if '(' == ch:  # 左括号
        stack.append(i)
    elif len(stack) > 1:  # 右括号，且有成对左括号
        stack.pop()  # 成对匹配
        ans = max(ans, i - stack[-1])
    else:  # 非法的右括号
        stack[0] = i
print(ans)
print()