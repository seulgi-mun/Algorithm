import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [0] * (n+1)

def bfs(x, y):
    q = deque([x])
    visited[x] = 1

    while q:
        t = q.popleft()

        for i in graph[t]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                cnt[i] = cnt[t] + 1


graph = [[] for _ in range(n+1)]
cnt = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)
bfs(a, b)
if cnt[b] > 0:
    print(cnt[b])
else:
    print(-1)