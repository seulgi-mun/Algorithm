def solution(numlist, n):
    answer = []

    gap = []

    for i in numlist:
        if i == n:
            answer.append(i)
        else:
            gap.append([i, abs(i - n)])

    gap.sort(key=lambda x: (x[1], -x[0]))

    for num, g in gap:
        answer.append(num)

    return answer