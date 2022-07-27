import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
# print(n, m)

for i in range(1, m+1):
    print(0, i)
    # 3-4 4-5
for j in range(m, n-1):
    print(j, j+1)
