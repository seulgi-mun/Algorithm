import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

for i in range(a, b+1):
    print(i)