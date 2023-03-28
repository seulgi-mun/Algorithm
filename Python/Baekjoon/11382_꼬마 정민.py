import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))
print(sum(num))