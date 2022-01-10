import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [0] * (n+10)

dp[1] = 1
dp[2] = 1
dp[3] = 1


# -1로 뺏을 경우가 가장 경우의 수가 많음
for k in range(4, n+10):
    dp[k] = k - 1
# print(dp)

for i in range(4, n+10):
    pass

# print(6 // 3)


"""
x*3 x*2 x+1 => n

1 %3 or %2 > 1
2 -1 or % 2 > 1
3 %3 > 1
4 -1 (dp[3]) or %2 %2 > 2
5 -1 (dp[4]) > 3
6 -1 (dp[5])
  %3(dp[3]) %2(dp[2]) > 2
7 -1 %3 %2(dp[6]) > 3
8 %2 %2(dp[4]) %2 > 3
9 %3 %3 > 2
10 -1 9%3 3%3 > 3
"""