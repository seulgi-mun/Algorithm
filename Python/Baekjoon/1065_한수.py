import sys
sys.stdin = open('input.txt')

n = int(input())

cnt = 0
for i in range(1, n+1):
    if 100 < i < 1000:
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            cnt += 1
    elif i < 100:
        cnt += 1
    elif i <= 10:
        cnt += 1
print(cnt)