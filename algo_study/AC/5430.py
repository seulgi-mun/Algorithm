import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    fx = list(map(str, input()))
    # print(fx)
    flag = 0
    status = 0

    num = int(input())
    arr = input()[1:-1].split(',')
    # print(arr)

    for i in range(len(fx)):
        # 뒤집기 한 번
        if fx[i] == 'R':
            # 안 뒤집 었으면 뒤집
            if status == 0:
                status = 1
            # R을 더 만난 경우 원래대로
            else:
                status = 0

        # 빼줄 때
        if fx[i] == 'D':
            if len(arr) == 0:
                print('error')
                # exit()
                break
            arr.pop()

    if status == 1:
        print(arr[::-1])
    else:
        print(arr)
