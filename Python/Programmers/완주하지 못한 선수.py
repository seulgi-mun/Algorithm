def solution(participant, completion):
    answer = ''

    athlete = {}

    for i in participant:
        if i not in athlete:
            athlete[i] = 1
        else:
            athlete[i] += 1

    for i in completion:
        athlete[i] -= 1

    for k, v in athlete.items():
        if v >= 1:
            answer += k

    return answer