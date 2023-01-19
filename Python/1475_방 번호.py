import sys
sys.stdin = open('input.txt')

n = input()

new_n = ''
for i in n:
    if i == '9':
        new_n += '6'
    else:
        new_n += i

cnt = 0
num = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
for i in new_n:
    num[i] += 1
num['6'] = (num['6'] + 1) // 2
# print(num)

maxx = 0
for k, v in num.items():
    if maxx <= v:
        maxx = v
print(maxx)


