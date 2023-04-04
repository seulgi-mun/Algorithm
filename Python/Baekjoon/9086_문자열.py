import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    s = input()
    print(s[0], s[-1], sep='')