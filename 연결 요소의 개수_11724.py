import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

stack = []

def bfs(x):
    global cnt
    q = deque([x])
    # print(q)
    visited[x] = 1

    while q:
        t = q.popleft()

        for i in graph[t]:
            # print(i)
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)



for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for j in range(1, n+1):
    if visited[j] == 0:
        if not graph[j]:
            cnt += 1
            visited[j] = 1
        else:
            bfs(j)
            cnt += 1

print(cnt)
# print(graph)
