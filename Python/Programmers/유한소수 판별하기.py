from fractions import Fraction


def solution(a, b):
    answer = 0

    div = Fraction(a, b)
    down = div.denominator

    while True:
        if down == 0:
            answer = 1
            break

        if down % 2 == 0:
            down = down // 2
        elif down % 5 == 0:
            down = down // 2
        else:
            answer = 2

    return answer