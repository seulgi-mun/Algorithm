import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def bfs():
    while q:
        s, e = q.popleft()

        for k in range(4):
            nx = s + dx[k]
            ny = e + dy[k]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[s][e] + 1
                q.append([nx, ny])


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    day = max(day, max(i))
print(day-1)