import sys
sys.stdin = open('input.txt')

n = input()

time = 0

for i in n:
    if i in 'ABC':
        time += 3
    elif i in 'DEF':
        time += 4
    elif i in 'GHI':
        time += 5
    elif i in 'JKL':
        time += 6
    elif i in 'MNO':
        time += 7
    elif i in 'PQRS':
        time += 8
    elif i in 'TUV':
        time += 9
    else:
        time += 10
print(time)