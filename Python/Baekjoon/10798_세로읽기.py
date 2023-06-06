import sys
sys.stdin = open('input.txt')

arr = [list(input()) for _ in range(5)]

tmp = ''

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            tmp += arr[j][i]
print(tmp)