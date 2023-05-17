def solution(name, yearning, photo):
    answer = []

    point = {}

    for i in name:
        if i not in point:
            point[i] = 0

    for i in range(len(yearning)):
        point[name[i]] = yearning[i]

    for i in photo:
        cnt = 0
        for j in i:
            if j in point:
                cnt += point[j]
        answer.append(cnt)

    return answer