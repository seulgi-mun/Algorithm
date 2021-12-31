import sys
sys.stdin = open('input.txt')
from pprint import pprint

n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(n+1)]
# print(dp)

for i in range(n+1):
    dp[i][0] = 1
    dp[i][i] = 1

# pprint(dp)
for x in range(1, n+1):
    for y in range(1, n+1):
        dp[x][y] = dp[x-1][y] + dp[x-1][y-1]

print(dp[n-1][k-1])
# pprint(dp)