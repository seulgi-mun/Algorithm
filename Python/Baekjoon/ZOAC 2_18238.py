import sys
sys.stdin = open('input.txt')

word = input()

start = 'A'
time = 0

for i in word:
    tmp = abs(ord(i) - ord(start))
    start = i
    time += min(tmp, 26 - tmp)

print(time)

