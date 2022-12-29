import sys
sys.stdin = open('input.txt')

T = int(input())

plan = []
for tc in range(T):
    s, e = map(int, input().split())
    # print(s, e)
    plan.append([s, e])
print(plan)
calendar = []
print(calendar)