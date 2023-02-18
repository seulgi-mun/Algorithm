def solution(balls, share):
    answer = 0

    up = 1
    for i in range(1, balls + 1):
        up *= i

    down = 1
    for i in range(1, balls - share + 1):
        down *= i

    mpack = 1
    for i in range(1, share + 1):
        mpack *= i
    answer = up / (down * mpack)

    return answer