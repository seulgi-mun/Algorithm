import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

tmp = {}
for i in num:
    if i not in tmp:
        tmp[i] = 1
    else:
        tmp[i] += 1

cnt = []
for k, v in tmp.items():
    cnt.append([k, v])
cnt.sort(key=lambda x: x[1], reverse=True)

print(round(sum(num)/n))
print(num[int(n/2)])
if n == 1:
    print(*num)
elif n >= 2:
    if cnt[0][1] != cnt[1][1]:
        print(cnt[0][0])
    else:
        print(cnt[1][0])
print(max(num) - min(num))