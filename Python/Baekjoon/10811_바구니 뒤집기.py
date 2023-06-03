import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

ball = list(range(1, n+1))

for _ in range(m):
    s, e = map(int, input().split())
    ball = ball[:s-1] + ball[s-1:e][::-1] + ball[e:]
print(*ball)