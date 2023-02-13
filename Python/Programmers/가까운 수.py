def solution(array, n):
    answer = 0

    gap = []
    for i in range(len(array)):
        gap.append([abs(array[i] - n), array[i]])

    gap.sort(key=lambda x: (x[0], x[1]))
    answer = gap[0][1]

    return answer