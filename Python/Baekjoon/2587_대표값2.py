import sys
sys.stdin = open('input.txt')

num = [int(input()) for _ in range(5)]
num.sort()
print(int(sum(num)/5))
print(num[int(len(num)/2)])