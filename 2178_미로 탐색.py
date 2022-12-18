import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append([x, y])
    # visited[x][y] = 1
    maze[x][y] = 0

    while q:
        for _ in range(len(q)):
            f, s = q.popleft()

            for k in range(4):
                nx = f + dx[k]
                ny = s + dy[k]

                # print(nx, ny)
                if f == n-1 and s == m-1:
                    return cnt + 1
                    # cnt += 1

                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    # cnt += 1
                    maze[nx][ny] = 0
                    q.append([nx, ny])
                    # visited[nx][ny] = visited[f][s] + 1
                    # pprint(visited)
                    # pprint(maze)
        cnt += 1
    return cnt


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
# print(maze)

visited = [[0] * m for _ in range(n)]

cnt = 1

bfs(0, 0)
# print(bfs(0, 0))
print(cnt)
