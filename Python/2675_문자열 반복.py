import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    n, w = input().split()
    # print(n, w)
    n = int(n)
    res = ''
    for i in w:
        res += i * n
    print(res)