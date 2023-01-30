import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
tmp = [0] * (max(arr) + 1)
ans = 0

while e < n:
    if tmp[arr[e]] < k:
        tmp[arr[e]] += 1
        e += 1
    else:
        tmp[arr[s]] -= 1
        s += 1
    ans = max(ans, e-s)
print(ans)