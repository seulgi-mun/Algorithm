import sys
sys.stdin = open('input.txt')

n = int(input())
w = []
for _ in range(n):
    w.append(int(input()))
w.sort(reverse=True)
# print(w)

for i in range(n):
    w[i] = w[i] * (i+1)
print(max(w))

""" 
w/k
10 / 2 > 5 
15 / 2 > 7.5
"""