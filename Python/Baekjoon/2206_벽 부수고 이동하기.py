import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

arr = [input().split() for _ in range(n)]
# print(arr)