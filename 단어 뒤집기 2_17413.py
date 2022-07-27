import sys
sys.stdin = open('input.txt')
from collections import deque

word = list(input())
# print(word)
q = deque(word)

temp = ''
stack = []

flag = 0

while q:
    t = q.popleft()
    # < 있으면 안뒤집게

    if t == '<':
        if len(temp) != 0:
            print(temp[::-1], end='')
            temp = ''
        # temp += t
        print(t, end='')
        flag = 1
        continue
        # > 만나면 상태 원래대로
    if t == '>' and flag == 1:
        flag = 0
        temp += t
        print(temp, end='')
        temp = ''
        continue
    if t == ' ':
        if flag == 1:
            print(temp, end=' ')
            temp = ''
        else:
            print(temp[::-1], end=' ')
            temp = ''
            continue
    else:
        temp += t

print(temp[::-1])
# print(*stack)
#
# result = ''
# for i in stack:
#     result += i
# print(result)