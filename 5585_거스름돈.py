import sys
sys.stdin = open('input.txt')


n = int(input())

change = [500, 100, 50, 10, 5, 1]

pay = 1000 - n

cnt = 0
for i in change:
    if pay // i:
        cnt += pay // i
        pay = pay % i
        # print(pay)
print(cnt)