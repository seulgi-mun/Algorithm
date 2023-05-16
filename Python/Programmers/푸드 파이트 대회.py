def solution(food):
    answer = ''

    center = 0
    left = ''

    for idx, key in enumerate(food):
        center += key // 2
        if idx >= 1:
            for _ in range(key // 2):
                left += str(idx)

    right = left[::-1]
    answer = left + '0' + right
    return answer