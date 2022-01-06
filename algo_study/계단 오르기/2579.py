import sys
sys.stdin = open('input.txt')

n = int(input())

stair = [0] * (n+10)

for k in range(1, n+1):
    stair[k] = int(input())

dp = [0] * (n+10)
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]


for i in range(3, n+10):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
print(dp[n])
