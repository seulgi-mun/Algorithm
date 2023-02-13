def solution(s):
    answer = ''

    once = {}

    for i in s:
        if i not in once:
            once[i] = 1
        else:
            once[i] += 1

    tmp = []
    for k, v in once.items():
        if v == 1:
            tmp.append(k)
    tmp.sort()

    for i in tmp:
        answer += i

    return answer