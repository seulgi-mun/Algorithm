import sys
sys.stdin = open('input.txt')

while True:
    n = int(input())
    if n == -1:
        break

    tmp = []
    for i in range(1, n):
        if n % i == 0:
           tmp.append(i)

    res = ''
    if sum(tmp) == n:
        for j in range(len(tmp)):
            res += str(tmp[j])
            if j != len(tmp)-1:
                res += ' + '

    if res:
        print(n, '=', res)
    else:
        print(n, 'is NOT perfect.')