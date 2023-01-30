import sys
sys.stdin = open('input.txt')

h, m = map(int, input().split())
time = int(input())

total = (h*60) + m + time

h = (total // 60) % 24
m = total % 60
print(h, m)