def solution(lottos, win_nums):
    answer = []

    maxx = 0
    minn = 0

    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    zero = lottos.count(0)

    if zero == 6:
        return [1, 6]

    for i in win_nums:
        if i in lottos:
            maxx += 1
            minn += 1

    if maxx == 6:
        return [1, 1]

    many = maxx + zero

    answer.append(score[many])
    answer.append(score[minn])

    return answer