import sys
sys.stdin = open('input.txt')


n = int(input())
a = list(map(int, input().split()))

new_a = sorted(a)

p = []

for i in range(n):
    idx = new_a.index(a[i])
    p.append(idx)
    new_a[idx] = -1
print(*p)