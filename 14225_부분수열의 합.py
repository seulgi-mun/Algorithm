import sys
sys.stdin = open('input.txt')
from itertools import combinations

n = int(input())
s = list(map(int, input().split()))

hap = set()
for i in range(1, n+1):
    arr = combinations(s, i)

    for j in arr:
        hap.add(sum(j))


tmp = set(range(1, max(hap)+1))

res = tmp - hap
if tmp != hap:
    print(min(res))
else:
    print(max(hap) + 1)