import sys
sys.stdin = open('input.txt')

n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

tmp = n
for i in people:
    i -= b
    if i > 0:
        if i % c:
            tmp += (i // c) + 1
        else:
            tmp += (i // c)
print(tmp)
