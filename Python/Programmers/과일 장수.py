def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)

    apple = []
    for i in range(0, len(score), m):
        if len(score[i:i + m]) >= m:
            apple.append(min(score[i:i + m]))

    for i in apple:
        answer += i * m

    return answer