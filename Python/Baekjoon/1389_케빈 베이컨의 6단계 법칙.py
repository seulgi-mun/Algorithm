import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = 1

    while q:
        t = q.popleft()

        for i in graph[t]:
            if visited[i] == 0:
                visited[i] = visited[t] + 1
                q.append(i)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = []
for i in range(1, n+1):
    visited = [0] * (n + 1)
    bfs(i)
    result.append(sum(visited))
print(result.index(min(result))+1)