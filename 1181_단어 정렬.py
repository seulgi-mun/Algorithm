import sys
sys.stdin = open('input.txt')

n = int(input())
word = set(input() for _ in range(n))
# print(word)
ls_word = list(word)
# print(ls_word)
tmp = []
for i in range(len(ls_word)):
    tmp.append([ls_word[i], len(ls_word[i])])
# print(tmp)

tmp.sort(key=lambda x: (x[1], x[0]))

for x, y in tmp:
    print(x)