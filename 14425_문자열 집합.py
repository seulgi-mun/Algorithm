import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
s = set(input() for _ in range(n))
check = [input() for _ in range(m)]
# print(check)

cnt = 0
for i in check:
    if i in s:
        cnt += 1
print(cnt)