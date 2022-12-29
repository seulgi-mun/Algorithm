import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
doll = list(map(int, input().split()))

ans = int(1e9)

ryan = []
for i in range(n):
    if doll[i] == 1:
        ryan.append(i)
# print(ryan)

s = 0
e = k-1     # 라이언 인형 수

if len(ryan) < k:
    print(-1)
    exit()

while True:
    tmp = ryan[e] - ryan[s] + 1
    ans = min(ans, tmp)

    if e == len(ryan)-1:
        break
    s += 1
    e += 1
print(ans)