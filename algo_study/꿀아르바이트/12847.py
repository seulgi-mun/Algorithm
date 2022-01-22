import sys
sys.stdin = open('input.txt')

rent, workday = map(int, input().split())
money = list(map(int, input().split()))

sub = []
temp = 0
for i in range(workday):
    temp = sum(money[i:workday+i])
    sub.append(temp)
print(max(sub))