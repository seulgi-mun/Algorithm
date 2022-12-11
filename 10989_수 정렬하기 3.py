import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
num = []
for _ in range(n):
    x = int(input())
    num.append(x)
num.sort()

for i in num:
    print(i)