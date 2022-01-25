import sys
sys.stdin = open('input.txt')

doll, ryan = map(int, input().split())
mix = list(map(int, input().split()))
# print(mix)
# apeach = 2 ryan = 1
arr = []
temp = 0
cnt = 0
find_ryan = 0
end = 0

for i in range(doll):
    while find_ryan < ryan and end < doll:
        if mix[end] == 1:
            find_ryan += 1
            end += 1
        arr.append(mix[end])