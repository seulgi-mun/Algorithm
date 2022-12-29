import sys
sys.stdin = open('input.txt')

n = int(input())

res = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))

    # print(num)
    res = sum(num) + i
    # print(res)
    if res == n:
        print(i)
        break
    elif i == n:
        # print(i , '?')
        print(0)
        break
