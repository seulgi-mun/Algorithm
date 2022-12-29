import sys
sys.stdin = open('input.txt')
from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0 for i in range(f+1)]
ans = [0] * (f+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        t = q.popleft()

        if t == g:
            return ans[g]

        for i in (t+u, t-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                ans[i] = ans[t] + 1
                q.append(i)

    if ans[g] == 0:
        return 'use the stairs'

print(bfs(s))
