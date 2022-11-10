import sys
sys.stdin = open('input.txt')

n = int(input())

stack = []
result = []
flag = 0
cnt = 1

for i in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    print('\n'.join(result))