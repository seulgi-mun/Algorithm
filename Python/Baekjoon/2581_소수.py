import sys
sys.stdin = open('input.txt')

m = int(input())
n = int(input())

res = []
for i in range(m, n+1):
    cnt = 0
    j = 2
    tmp = i
    while True:
        if tmp == 1:
            break

        if tmp % j == 0:
            cnt += 1
            tmp = tmp // j
        else:
            j += 1
    if cnt < 2 and i != 1:
        res.append(i)
    # print(res)
# print(res)
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)