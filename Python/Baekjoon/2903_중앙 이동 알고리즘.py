import sys
sys.stdin = open('input.txt')

n = int(input())
ori = 2
dp = [0] * (n+5)
dp[0] = 2
dp[1] = 3
dp[2] = 5
# print(2**(n-1),'??')
for i in range(3, n+1):
    dp[i] = dp[i-1] + 2**(i-1)
print(dp[n]*dp[n])
# print(dp)