import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

tmp = []
for i in range(1, n+1):
    if n % i == 0:
        tmp.append(i)

try:
    print(tmp[k-1])
except:
    print(0)