import sys
sys.stdin = open('input.txt')

"""
현재 회의가 끝나는 시간이 제일 늦은 회의 시작 시간보다 크면
더 이상 회의를 할 수 없는 상황이므로 여태까지 회의에 참여한 인원수를 리스트에 추가해준다
"""

n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]
info.sort()
# print(info)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = info[0][2]

for i in range(2, n+1):
    dp[i] = max(dp[i-2] + info[i-1][2], dp[i-1])
print(dp[-1])