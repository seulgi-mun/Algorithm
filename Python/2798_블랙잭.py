import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
card = list(map(int, input().split()))

tmp = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                tmp = max(tmp, card[i] + card[j] + card[k])
print(tmp)