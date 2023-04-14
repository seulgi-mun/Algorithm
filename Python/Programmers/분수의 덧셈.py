from fractions import Fraction


def solution(numer1, denom1, numer2, denom2):
    answer = []

    up = (numer1 * denom2) + (numer2 * denom1)
    down = denom1 * denom2

    # print(up, down)

    for i in range(10001, 0, -1):
        if up % i == 0 and down % i == 0:
            up = up // i
            down = down // i

    answer.append(up)
    answer.append(down)

    return answer