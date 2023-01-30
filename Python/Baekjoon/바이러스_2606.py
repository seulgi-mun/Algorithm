import sys
sys.stdin = open('input.txt')
from collections import deque

cpu = int(input())
n = int(input())

graph = [[] for _ in range(cpu+1)]

visitied = [0] * (cpu+1)


def bfs(x):
    global cnt
    q = deque([x])
    visitied[1] = 1
    # q.append()
    # print(q)
    while q:
        t = q.popleft()
        # print(t)
        for i in t:
            # print(i)
            if visitied[i] == 0 and graph[i]:
                visitied[i] = 1
                q.append(graph[i])
                bfs(graph[i])
                cnt += 1

for _ in range(n):
    m, v = map(int, input().split())
    graph[m].append(v)
    graph[v].append(m)
    cnt = 0
bfs(graph[1])
print(cnt)
# print(graph)