import sys
sys.stdin = open('input.txt')
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def dfs(x):
    print(x, end='')
    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
            visited[i] = 1


def bfs(y):
    q = deque([y])
    visited[y] = 1

    while q:
        t = q.popleft()
        print(t, end='')

        for j in graph[t]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)