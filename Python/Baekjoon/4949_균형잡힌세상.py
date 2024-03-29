import sys
sys.stdin = open('input.txt')

while True:
    words = input()
    stack = []
    if words == '.':
        break

    for i in words:

        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if stack:
        print('no')
    else:
        print('yes')