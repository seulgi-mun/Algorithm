import sys
sys.stdin = open('input.txt')

while True:
    n = int(input())
    a = [True] * (2*n+1)
    # print(a)
    if n == 0:
        break

    for i in range(2, 2*n+1):
        if a[i]:
            for j in range(i+i, 2*n+1, i):
                a[j] = False

    a[1] = False
    cnt = 0
    for i in range(n+1, 2*n+1):
        if a[i]:
            cnt += 1
    print(cnt)
