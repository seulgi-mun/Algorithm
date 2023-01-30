import sys
sys.stdin = open('input.txt')

n, x = map(int, input().split())
visit = list(map(int, input().split()))

tmp = sum(visit[0:x])
ans = tmp
cnt = 1
for i in range(x, n):
    ans -= visit[i-x]
    ans += visit[i]
    if ans > tmp:
        tmp = ans
        cnt = 1
    elif ans == tmp:
        cnt += 1

if max(visit) == 0:
    print('SAD')
else:
    print(tmp)
    print(cnt)