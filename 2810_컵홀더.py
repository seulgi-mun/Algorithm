import sys
sys.stdin = open('input.txt')

n = int(input())
seat = input()

check = {'S': 0, 'L': 0}

tmp = '*'
l_cnt = 0
for i in seat:
    if i == 'S':
        tmp += 'S*'
    else:
        l_cnt += 1
        if l_cnt == 2:
            tmp += 'LL'
            tmp += '*'
            l_cnt = 0

if tmp.count('*') >= n:
    print(n)
else:
    print(tmp.count('*'))
