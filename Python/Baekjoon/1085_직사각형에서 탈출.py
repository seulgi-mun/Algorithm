import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, input().split())

ans = 0
ans = min(abs(w-x), abs(y-h), (x-0), (y-0))
print(ans)