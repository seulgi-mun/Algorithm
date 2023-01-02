import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(sys.stdin.readline())

# stack = deque([])
stack = []
idx = 0
for _ in range(n):
    order = sys.stdin.readline().split()
    # print(order)
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'size':
        print(len(stack)-idx)
    elif order[0] == 'pop':
        if len(stack) > idx:
            print(stack[idx])
            idx += 1
        else:
            print(-1)
    elif order[0] == 'empty':
        if len(stack) != idx:
            print(0)
        else:
            print(1)
            idx = 0
            stack = []
    elif order[0] == 'front':
        if len(stack) > idx:
            print(stack[idx])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(stack) > idx:
            print(stack[-1])
        else:
            print(-1)
