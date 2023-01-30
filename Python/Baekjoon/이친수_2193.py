import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [0] * (n + 10)

dp[1] = 1
dp[2] = 1


for i in range(3, n+10):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


# temp = []
# for i in range(7):
#     temp.append(bin(i)[2:])
# print(temp)