import sys
sys.stdin = open('input.txt')

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: (x[1], x[0]))

cnt = 1
e = info[0][1]

for i in range(1, n):
    if e <= info[i][0]:
        e = info[i][1]
        cnt += 1
print(cnt)