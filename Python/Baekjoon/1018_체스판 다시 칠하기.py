import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

chess = [list(input()) for _ in range(n)]

res = []
for i in range(n - 7):
    for j in range(m - 7):
        black = 0
        white = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] == 'W':
                        white += 1
                    if chess[x][y] == 'B':
                        black += 1
                else:
                    if chess[x][y] == 'B':
                        white += 1
                    if chess[x][y] == 'W':
                        black += 1
        res.append(min(black, white))

print(min(res))
