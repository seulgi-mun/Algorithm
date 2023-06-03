import sys, math
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    res = math.lcm(a, b)
    print(res)
