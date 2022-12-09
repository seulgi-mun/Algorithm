import sys
sys.stdin = open('input.txt')

a = [0, 0] + [1] * 10002
for i in range(2, 10002):
    if a[i]:
        for j in range(i+i, 10002, i):
            a[j] = 0
# print(a)

t = int(input())

for _ in range(t):
    n = int(input())
    x = n // 2
    y = x
    # print(x, y)

    while x > 0:
        if a[x] and a[y]:
            print(x, y)
            break
        else:
            x -= 1
            y += 1
