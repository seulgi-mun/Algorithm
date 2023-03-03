import sys
sys.stdin = open('input.txt')

while True:
    n = int(input())
    if n == 0:
        break
    words = []
    for _ in range(n):
        ori = input()
        new = ori.lower()
        words.append([new, ori])
    words.sort()

    print(words[0][1])
