import sys
sys.stdin = open('input.txt')

piece = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))
# print(n)
tmp = [0] * len(n)
for i in range(len(n)):
    if n[i] <= piece[i]:
        tmp[i] = piece[i] - n[i]
    else:
        tmp[i] = piece[i] - n[i]
print(*tmp)