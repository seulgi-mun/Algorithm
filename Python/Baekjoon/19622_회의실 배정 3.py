import sys
sys.stdin = open('input.txt')

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
# print(time_table)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = time_table[0][2]

for i in range(2, n+1):
    dp[i] = max(dp[i-2] + time_table[i-1][2], dp[i-1])
# print(dp)
print(dp[-1])