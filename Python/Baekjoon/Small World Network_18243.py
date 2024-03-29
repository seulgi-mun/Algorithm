import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [-1] * (n+1)


for _ in range(k):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

print(graph)