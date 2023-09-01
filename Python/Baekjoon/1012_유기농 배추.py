from collections import deque

import sys
sys.stdin = open('input.txt')


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    # visited[x][y]

    while q:
        tt = q.popleft()
        # visited[tt[0]][tt[1]] = 1

        for k in range(4):
            nx = tt[0] + dx[k]
            ny = tt[1] + dy[k]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and land[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx, ny])

def dfs(x, y):
    visited[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and land[nx][ny] == 1:
            dfs(nx, ny)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    land = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        j, i = map(int, input().split())
        land[i][j] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                # dfs(i, j)
                bfs(i, j)
                ans += 1
    print(ans)