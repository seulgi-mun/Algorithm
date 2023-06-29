import sys, math
sys.stdin = open('input.txt')

n = int(input())
arr = [1] * (n+1)
for i in range(1, n+1):
    if arr[i]:
        arr[i] = 0
    else:
        arr[i] = 1
print(arr)