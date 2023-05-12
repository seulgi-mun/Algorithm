def solution(array, commands):
    answer = []

    for s, e, f in commands:
        tmp = array[s - 1:e]
        tmp.sort()
        answer.append(tmp[f - 1])

    return answer