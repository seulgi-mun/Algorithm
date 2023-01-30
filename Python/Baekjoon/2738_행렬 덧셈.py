import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
# print(a)
res = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = a[i][j] + b[i][j]

for i in res:
    print(*i)