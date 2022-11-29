import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(28)]
# arr.sort()
# print(arr)

res = []
for i in range(1, 31):
    if i not in arr:
        res.append(i)
res.sort()
print(res[0])
print(res[1])