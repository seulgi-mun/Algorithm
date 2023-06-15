import sys
sys.stdin = open('input.txt')

def gcdd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

n = int(input())
num = [int(input()) for _ in range(n)]

gap = []
for i in range(len(num)-1):
    gap.append(abs(num[i+1] - num[i]))

set_gap = list(set(gap))

tmp = set_gap[0]
for i in range(1, len(set_gap)):
    tmp = gcdd(tmp, set_gap[i])

res = 0
for i in gap:
    res += i // tmp - 1
print(res)
