def solution(dots):
    answer = 0

    width = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]

    answer = width * height

    return answer