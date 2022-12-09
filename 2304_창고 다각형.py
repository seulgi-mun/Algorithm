import sys
sys.stdin = open('input.txt')

n = int(input())

arr = [0] * 1001
max_h = 0
width = 0
max_h_idx = 0
for _ in range(n):
    l, h = map(int, input().split())
    arr[l] = h
    if max_h < h:
        max_h = h
        max_h_idx = l
    if width < l:
        width = l
# print(arr)

height = 0
total = 0

for i in range(max_h_idx+1):
    if height < arr[i]:
        height = arr[i]
        total += height
    else:
        total += height

height = 0
for i in range(width, max_h_idx, -1):
    if height < arr[i]:
        height = arr[i]
        total += height
    else:
        total += height
print(total)