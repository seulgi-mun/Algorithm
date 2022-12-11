import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)

print(min(score[:k]))