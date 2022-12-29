import sys
sys.stdin = open('input.txt')

a, b, v = map(int, input().split())

goal = (v-b) / (a-b)
if goal == int(goal):
    print(int(goal))
else:
    print(int(goal) + 1)