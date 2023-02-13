def solution(emergency):
    answer = []

    tmp = {}
    order = sorted(emergency, reverse=True)

    for idx, num in enumerate(order):
        tmp[num] = idx + 1

    for i in emergency:
        answer.append(tmp[i])
    return answer