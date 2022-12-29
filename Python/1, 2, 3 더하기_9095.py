import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0] * (n + 10)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # print(dp)
    for i in range(4, n+10):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
    # print(dp)

"""
0 0 1 3 7 13

5 > 13
1 + 2 + 3

1 1 1 1 1 > 1
1 1 1 2 > 1
1 1 2 1 > 1
1 2 1 1 > 1
2 1 1 1 > 1
1 1 3 > 1
1 3 1 > 1
3 1 1 > 1
2 3 > 1
3 2 > 1
1 1 2 > 1
1 2 1 > 1
2 1 1 > 1
"""