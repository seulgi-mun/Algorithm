import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(99999)
from collections import deque


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x, y, s, e):
    global cnt
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        xx, yy = q.popleft()

        if xx == s and yy == e:
            # print(xx)
            # visited[xx][yy] = 1
            return visited[xx][yy] - 1

        for k in range(8):
            nx = xx + dx[k]
            ny = yy + dy[k]

            if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == 0:
                visited[nx][ny] = visited[xx][yy] + 1
                q.append([nx, ny])
                # pprint(visited)

    # return visited[s][e]


t = int(input())

for _ in range(t):
    length = int(input())
    now_x, now_y = map(int, input().split())
    go_x, go_y = map(int, input().split())
    chess = [[0] * length for _ in range(length)]
    visited = [[0] * length for _ in range(length)]

    cnt = 0
    print(bfs(now_x, now_y, go_x, go_y))
