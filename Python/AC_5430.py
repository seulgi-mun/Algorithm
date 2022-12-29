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


"""
# deque 쓸 때
import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    word = input()
    n = int(input())
    nums = input()[1:-1].split(',')

    q = deque(nums)
    flag = 0

    # 빈 배열이면 초기화
    if n == 0:
        q = []

    for i in word:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                # 두번 뒤집은 거면 원래상태니까 그냥 맨 앞에꺼 빼기
                if flag % 2  == 0:
                    q.popleft()
                else:
                    q.pop()


    else:
        # R이 2번이면 원상태로 출력
        if flag % 2 == 0:
            print('[' + ','.join(q) + ']')
        # 아니면 뒤집기
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')
            
"""