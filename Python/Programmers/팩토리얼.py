def solution(n):
    answer = 0

    tmp = 1
    for i in range(1, n + 1):
        tmp = tmp * i
        if tmp == n:
            answer = i
            break
        else:
            if tmp <= n <= tmp * i:
                answer = i
                break

    return answer