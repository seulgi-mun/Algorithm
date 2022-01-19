import sys
sys.stdin = open('input.txt')

n = int(input())
root = 1

for _ in range(n-1):
    a, b = map(int, input().split())
    # print(a, b)