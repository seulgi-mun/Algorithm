import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(input())

q = deque()

while True:
    info = int(input())
    if len(q) < n:
        if info == 0:
            q.popleft()
        elif info == -1:
            break
        else:
            q.append(info)
    else:
        if info == 0:
            q.popleft()
    if info == -1:
        break

if q:
    print(*q)
else:
    print('empty')