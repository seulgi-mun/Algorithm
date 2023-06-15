import sys
sys.stdin = open('input.txt')

def gcdd(x, y):
    while y != 0:
        x, y = y, y % x
    return x

n = int(input())
num = [int(input()) for _ in range(n)]

gap = []
for i in range(len(num)-1):
    gap.append(abs(num[i+1] - num[i]))

tmp = gap[0]
for i in range(len(gap)-1):
    tmp = gcdd(tmp, gap[i])

res = 0
for i in gap:
    res += i // tmp - 1
print(res)
