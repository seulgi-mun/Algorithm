import sys
sys.stdin = open('input.txt')

n = int(input())

ans = ''
for _ in range(n//4):
    ans += 'long '
ans += 'int'
print(ans)