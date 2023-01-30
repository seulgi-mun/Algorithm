import sys
sys.stdin = open('input.txt')

n = int(input())
word = [input() for _ in range(n)]
cnt = 0

for i in word:
    stack = []
    for j in range(len(i)):
        if i.count(i[j]) == len(i):
            cnt += 1
            break
        elif i[j] not in stack or i[j] == stack[-1]:
            stack.append(i[j])
            if len(stack) == len(i):
                cnt += 1
print(cnt)
