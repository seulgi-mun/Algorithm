import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
# print(coin)

cnt = 0
for i in coin:
    cnt += k // i
    k %= i
print(cnt)