def solution(s):
    answer = 0

    ori = 1
    dif = 0

    g = 0
    e = 1
    for i in range(1, len(s)):
        if s[g] != s[i]:
            dif += 1
            if dif == ori:
                answer += 1
                g = i + 1
                e = i
        else:
            ori += 1

    # print(ori, dif)
    if ori != dif:
        answer += 1
    # print(s[g-1])

    return answer