import sys, math
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, r = map(int, input().split())

up = math.factorial(n)
down = (math.factorial(n-r) * math.factorial(r))

ans = (up // down) % 1000000007
print(ans)