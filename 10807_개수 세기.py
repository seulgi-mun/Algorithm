import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

print(arr.count(v))