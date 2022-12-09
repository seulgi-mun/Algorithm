import sys
sys.stdin = open('input.txt')

n, k, b = map(int, input().split())
broken = [int(input()) for _ in range(b)]

light = [1] * (n+1)

for i in broken:
    light[i] = 0
# print(light)
tmp = sum(light[1:k+1])
ans = k - tmp
for i in range(2, n-k+2):
    tmp = tmp - light[i-1] + light[i-1+k]
    ans = min(ans, k-tmp)
    if ans == 0:
        break
print(ans)