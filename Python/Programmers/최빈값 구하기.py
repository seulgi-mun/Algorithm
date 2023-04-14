def solution(array):
    answer = 0

    tmp = {}

    for i in array:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1

    cnt = 0
    maxx = max(tmp.values())
    max_key = 0
    for k, v in tmp.items():
        if maxx == v:
            max_key = k
            cnt += 1

    if cnt >= 2:
        answer = -1
    else:
        answer = max_key

    return answer