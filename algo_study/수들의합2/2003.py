import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
num = list(map(int, input().split()))
# print(num)

temp = 0
for i in range(m):
    temp = num[i] + num[i+1]
