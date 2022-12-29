import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())

a = [1] * (n+1)

for i in range(2, n+1):
    if a[i] == 1:
        for j in range(i+i, n+1, i):
            a[j] = 0
a[1] = 0

for i in range(m, n+1):
    if a[i] == 1:
        print(i)