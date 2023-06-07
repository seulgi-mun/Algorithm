import sys
sys.stdin = open('input.txt')

n = int(input())
cnt = 0
num = n-2
for i in range(1, n-1):
    cnt += (num * i)
    num -= 1
print(cnt)
print(3)