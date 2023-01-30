import sys
sys.stdin = open('input.txt')

n = input().upper()

word = {}
for i in n:
    if i not in word:
        word[i] = 1
    else:
        word[i] += 1
# print(word)
maxx = max(word.values())
# print(word.values())
tmp = 0
preq = ''
for k, v in word.items():
    if v == maxx:
        tmp += 1
        preq = k
if tmp >= 2:
    print('?')
else:
    print(preq)
