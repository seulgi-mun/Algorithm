def solution(n):
    answer = 0

    for i in range(6, 601, 6):
        if i % n == 0:
            answer += i // 6
            break
    return answer