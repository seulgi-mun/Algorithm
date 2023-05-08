from itertools import combinations


def solution(number):
    answer = 0

    for j in combinations(number, 3):
        if sum(j) == 0:
            answer += 1

    return answer