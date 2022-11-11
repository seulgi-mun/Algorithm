import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(99999)
from collections import deque

dx = [1, 2, 2, 1, -1, -1, -2, -2]
dy = [2, 1, -1, -2, 2, -2, 1, -1]

def bfs(x, y, g_x, g_y):
    global cnt
    q = deque()
    q.append((x, y))

    visited[x][y] = 1

    while q:
        s, e = q.popleft()

        if s == g_x and e == g_y:
            print(visited[g_x][g_y] - 1)
            return

        for k in range(8):
            nx = dx[k] + s
            ny = dy[k] + e
            # print(nx, ny, 'ddd')

            if 0 <= nx < l and 0 <= ny < l and  visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[s][e] + 1


t = int(input())

for _ in range(t):
    l = int(input())
    now_x, now_y = map(int, input().split())
    go_x, go_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    bfs(now_x, now_y, go_x, go_y)
