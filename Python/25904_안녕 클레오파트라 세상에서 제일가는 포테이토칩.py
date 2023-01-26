import sys
sys.stdin = open('input.txt')

n, x = map(int, input().split())
t = list(map(int, input().split()))
# print(t)

i = x
res = 0
while True:
    for j in t:
        if j >= i:
            i += 1
            continue
        else:
            print(t.index(j)+1)
            exit()
