import sys
sys.stdin = open('input.txt')

n, b = map(int, input().split())
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tmp = ''
while int(n) != 0:
    tmp += alpha[int(n) % b]
    n = int(n) // b
print(tmp[::-1])