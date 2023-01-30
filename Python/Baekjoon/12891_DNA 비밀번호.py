import sys
sys.stdin = open('input.txt')

s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

res = 0
ss = dna[:p]
tmp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in ss:
    tmp[i] += 1
# print(tmp)

cnt = 0
if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
    cnt += 1

s_idx = 0
e_idx = s_idx + p

for i in range(len(dna)-p):
    tmp[dna[s_idx+i]] -= 1
    tmp[dna[e_idx+i]] += 1
    if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
        cnt += 1
print(cnt)