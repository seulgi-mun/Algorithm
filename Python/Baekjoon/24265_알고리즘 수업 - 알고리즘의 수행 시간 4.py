import sys
sys.stdin = open('input.txt')

n = int(input())
tmp = 0
for i in range(1, n):
    tmp += i
print(tmp)
print(2)