import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)

max_num = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_num:
            max_num = arr[i][j]
            x = i+1
            y = j+1
print(max_num)
print(x, y)