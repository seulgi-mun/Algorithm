import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

visited = [0] * (n+10)
cnt = 1

def dfs(x):
    global cnt

    for nx in (x-arr[x], x+arr[x]):
        if 0 <= nx < n and visited[nx] == 0:
            visited[nx] = 1
            cnt += 1
            dfs(nx)

dfs(s-1)
print(cnt)