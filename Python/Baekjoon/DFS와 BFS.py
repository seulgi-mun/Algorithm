from collections import deque
import sys
sys.stdin = open('input.txt')

n, m, v = map(int, input().split())
vv = [[] for _ in range(n+10)]
visited1 = [0] * (n+10)
# print(visited)

for _ in range(m):
    a, b = map(int, input().split())
    vv[a].append(b)
    vv[b].append(a)

for i in vv:
    i.sort()

ans1 = []
def dfs(cur):
    for x in vv[cur]:
        if visited1[x]:
            continue
        visited1[x] = 1
        ans1.append(x)
        dfs(x)
visited1[v] = 1
ans1.append(v)
dfs(v)

visited2 = [0] * (n+10)

q = deque([v])
visited2[v] = 1
ans2 = [v]
while q:
    cur = q.popleft()
    for x in vv[cur]:
        if visited2[x]:
            continue
        visited2[x] = 1
        ans2.append(x)
        q.append(x)

print(*ans1)
print(*ans2)