def solution(n):
    answer = 0

    arr = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i + i, n + 1, i):
                arr[j] = False
    # print(arr)
    for i in range(1, n + 1):
        if arr[i] == True:
            answer += 1

    return answer