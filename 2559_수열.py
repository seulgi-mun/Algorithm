import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

tmp = sum(temperature[:k])
ans = tmp
for i in range(k, n):
    tmp -= temperature[i-k]
    tmp += temperature[i]

    if ans <= tmp:
        ans = tmp
print(ans)