import sys
sys.stdin = open('input.txt')

n = int(input())

pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append([x, y])
# print(pos)

pos.sort(key=lambda x: (x[0], x[1]))

for i in pos:
    print(*i)