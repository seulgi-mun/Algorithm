import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(5000)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

def dfs(x):
    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

cnt = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
