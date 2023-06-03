import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

tmp = a*b
while b > 0:
    a, b = b, a % b

print(tmp//a)