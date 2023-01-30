import sys
sys.stdin = open('input.txt')

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
time_table.sort(key=lambda x: (x[1], x[0]))
print(time_table)

dp = [0] * (n+1)
dp[0] = 0
# dp[1] = time_table[0][2]

# tmp = 0
for j in range(n-1):
    for i in range(j, n+1):
        if time_table[j+1][0] <= time_table[j][1]:
            continue
        print(time_table[j])
print(dp)