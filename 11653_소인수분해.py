import sys
sys.stdin = open('input.txt')

n = int(input())

res = []
i = 2
tmp = n
while True:
    if tmp == 1:
        break

    if tmp % i == 0:
        tmp = tmp // i
        res.append(i)
    else:
        i += 1

for i in res:
    print(i)