def solution(n):
    answer = ''

    n = sorted(str(n))

    for i in range(len(n) - 1, -1, -1):
        answer += n[i]

    return int(answer)