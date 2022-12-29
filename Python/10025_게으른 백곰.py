import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

arr = [0] * 1000001

for _ in range(n):
    ice, pos = map(int, input().split())
    arr[pos] = ice

s = 0
e = 2*k + 1

hap = sum(arr[s:e])
ans = hap

for i in range(e, len(arr)):
    hap -= arr[i-e]
    hap += arr[i]
    ans = max(ans, hap)
print(ans)