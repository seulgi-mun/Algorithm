import sys
sys.stdin = open('input.txt')

n = int(input())

chat = {}
cnt = 0
for _ in range(n):
    word = input()

    if word == 'ENTER':
        chat = {}
    else:
        if word not in chat:
            chat[word] = 1
            cnt += 1
print(cnt)