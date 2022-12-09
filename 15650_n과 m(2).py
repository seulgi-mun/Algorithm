import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

arr = []

def recur(cur):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(cur, n+1):
        if i not in arr:
            arr.append(i)
            recur(i+1)
            arr.pop()

recur(1)
# print(recur(0))