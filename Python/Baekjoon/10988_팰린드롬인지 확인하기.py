import sys
sys.stdin = open('input.txt')

n = input()

res = 1
for i in range(len(n)//2):
    if n[i] == n[-1-i]:
        continue
    else:
        res = 0
print(res)