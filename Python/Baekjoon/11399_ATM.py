import sys
sys.stdin = open('input.txt')

n = int(input())
p = list(map(int, input().split()))

time = []

for i in range(n):
    time.append((i+1, p[i]))

time.sort(key=lambda x: x[1])

tmp = []
cnt = 0
for k, v in time:
    cnt = cnt + v
    tmp.append(cnt)
print(sum(tmp))