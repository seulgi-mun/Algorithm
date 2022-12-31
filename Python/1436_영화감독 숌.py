import sys
sys.stdin = open('input.txt')

n = int(input())

six = '666'
tmp = []
six_cnt = 0
i = 0

while True:
    if six in str(i):
        tmp.append(i)
        six_cnt += 1
        if six_cnt == n:
            break
    i += 1
print(tmp[n-1])