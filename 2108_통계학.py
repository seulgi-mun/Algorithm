import sys
sys.stdin = open('input.txt')

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
# print(num)

tmp = {}
for i in num:
    if i not in tmp:
        tmp[i] = 1
    else:
        tmp[i] += 1
set_num = set(num)

preq = []
for i in set_num:
    preq.append(num.count(i))
print(preq.count(max(preq)), '?')
# print(tmp)
cnt = []
# gap = 0
for k, v in tmp.items():
    cnt.append([k, v])
cnt.sort(key=lambda x: x[1], reverse=True)
# print(cnt)

print(round(sum(num)/n))
print(num[n//2])
if n == 1:
    print(*num)
elif n >= 2:
    if preq.count(max(preq)) > 2:
        print(cnt[0][0])
    else:
        print(cnt[1][0])
print(max(num) - min(num))