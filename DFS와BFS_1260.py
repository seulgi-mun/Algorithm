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
