def solution(before, after):
    answer = 0

    b = {}
    a = {}

    for i in before:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1

    for j in after:
        if j not in a:
            a[j] = 1
        else:
            a[j] += 1

    if a == b:
        answer = 1
    else:
        answer = 0

    return answer