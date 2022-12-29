import sys
sys.stdin = open('input.txt')

n = int(input())
sang = set(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

res = {}
for i in card:
    if i in sang:
        res[i] = 1
    else:
        res[i] = 0

for k, v in res.items():
    print(v, end=' ')