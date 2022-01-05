import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [0] * (n + 10)

dp[1] = 1
dp[2] = 3

for i in range(3, n+10):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[n])