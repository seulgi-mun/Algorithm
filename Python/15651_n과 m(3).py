import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

arr = [0 for _ in range(m)]
def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(n):
        arr[cur] = i+1
        recur(cur+1)

recur(0)