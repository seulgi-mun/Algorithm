import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

ball = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    for x in range(i, j+1):
        ball[x] = k
print(*ball[1:])