import sys
sys.stdin = open('input.txt')

n = int(input())

info = []

for i in range(n):
    x, y = map(int, input().split())
    # print(x, y)
    info.append([x, y])

# print(info)

for i in info:
    grade = 1
    for j in info:
        if i != j:
            if i[0] < j[0] and i[1] < j[1]:
                # print(grade)
                grade += 1
    print(grade, end=' ')
