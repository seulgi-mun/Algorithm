import sys
sys.stdin = open('input.txt')

t = int(input())
# button = {'A': 300, 'B': 60, 'C': 10}
button = {'A': 0, 'B': 0, 'C': 0}


tmp = t
while True:
    if tmp == 0:
        print(*list(button.values()))
        break
    elif tmp < 10:
        print(-1)
        break

    elif tmp >= 300:
        tmp = tmp - 300
        button['A'] += 1
        # print(tmp, '300')

    elif tmp >= 60:
        tmp = tmp - 60
        button['B'] += 1
        # print(tmp, '60')

    elif tmp >= 10:
        tmp = tmp - 10
        button['C'] += 1
        # print(tmp, '10')
