import sys
sys.stdin = open('input.txt')


def sliding_window(ls, k):
    max_sum = 0
    start = 0
    temp = 0

    for key, val in enumerate(ls):
        temp += val

        if key - start + 1 == k:
            max_sum = temp
            temp -= ls[start]
            start += 1
    return max_sum


bucket, touch = map(int, input().split())

arr = [0] * (100)

for _ in range(bucket):
    ice, x = map(int, input().split())
    # print(ice, x)
    arr[x] = ice
print(arr)
print(sliding_window(arr, touch))