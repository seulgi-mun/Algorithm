import sys
sys.stdin = open('input.txt')

rent, workday = map(int, input().split())
money = list(map(int, input().split()))


def sliding_window(arr, k):
    max_sum = 0
    start = 0
    temp = 0

    # 뒤에 하나씩 더해 주는 구간 012 다음 123일 때 3번값 더함
    for key, val in enumerate(arr):
        temp += val

        if key - start + 1 == k:
            max_sum = max(max_sum, temp)
            # 앞에 하나씩 빼주는 구간 012 > 123 일 때 0 빼줌  
            temp -= arr[start]
            # 범위 이동
            start += 1

    return max_sum

print(sliding_window(money, workday))