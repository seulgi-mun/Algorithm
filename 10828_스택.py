import sys
sys.stdin = open('input.txt')

n = int(input())

stack = []
for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]
    # print(order)
    if 'push' == order:
        stack.append(word[1])
    elif order == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'size':
        print(len(stack))
    elif order == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif order == 'size':
        print(len(stack))