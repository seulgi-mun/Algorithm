import sys
sys.stdin = open('input.txt')
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_1 = [0] * (n+1)
visited_2 = [0] * (n+1)

def dfs(x):
    # print(x, '>>>>')
    visited_1[x] = 1
    print(x, end=' ')

    for i in graph[x]:
        if visited_1[i] == 0:
            visited_1[i] = 1
            dfs(i)

def bfs(y):
    q = deque([y])

    visited_2[y] = 1

    while q:
        t = q.popleft()
        print(t, end=' ')
        for i in graph[t]:
            if visited_2[i] == 0:
                visited_2[i] = 1
                q.append(i)


for _ in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(v)
print()
bfs(v)