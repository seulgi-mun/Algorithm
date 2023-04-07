from fractions import Fraction


def solution(a, b):
    answer = 0

    div = Fraction(a, b)
    b = div.denominator

    while b % 2 == 0:
        b = b // 2

    while b % 5 == 0:
        b = b // 5

    if b == 1:
        answer = 1
    else:
        answer = 2

    return answer