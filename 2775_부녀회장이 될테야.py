import sys
sys.stdin = open('input.txt')

t = int(input())

dp = [[0] * 20 for _ in range(20)]
dp[0][1] = 1
dp[0][2] = 2
dp[0][3] = 3

for i in range(4, 20):
    dp[0][i] = i

for _ in range(t):
    k = int(input())
    n = int(input())

    for i in range(1, 20):
        for j in range(20):
            dp[i][j] = sum(dp[i-1][0:j+1])
    print(dp[k][n])

