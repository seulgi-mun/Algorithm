def solution(n):
    answer = 0

    num = n ** (1 / 2)
    # print(num)

    if num % 1 == 0:
        # print(num % 1)
        answer = (num + 1) ** 2
    else:
        answer = -1

    return answer