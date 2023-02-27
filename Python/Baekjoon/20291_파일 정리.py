import sys
sys.stdin = open('input.txt')

n = int(input())
file = {}

for _ in range(n):
    name, typee = input().split('.')
    if typee not in file:
        file[typee] = 1
    else:
        file[typee] += 1

res = []
for k, v in file.items():
    res.append([k, v])

res.sort()
for i in res:
    print(*i)