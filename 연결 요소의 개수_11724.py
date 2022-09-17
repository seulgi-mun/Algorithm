import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


def bfs(x):
    global cnt
    q = deque([x])
    # print(q)
    visited[x] = 1




for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 0


