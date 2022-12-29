import sys
sys.stdin = open('input.txt')

n = list(input())

num = []
for i in n:
    num.append(int(i))

num.sort(reverse=True)
for i in num:
    print(i, end='')