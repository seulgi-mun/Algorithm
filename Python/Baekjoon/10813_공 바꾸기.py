import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

ball = list(range(n+1))
for _ in range(m):
    i, j = map(int, input().split())
    ball[i], ball[j] = ball[j], ball[i]

for i in range(1, len(ball)):
    print(ball[i], end=' ')