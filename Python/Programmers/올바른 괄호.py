def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if stack:
            if stack[-1] == '(':
                if s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    # print(stack)
    if stack:
        answer = False

    return answer