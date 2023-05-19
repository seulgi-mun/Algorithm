def solution(number, limit, power):
    answer = 0

    divisor = [0 for _ in range(number + 1)]
    for i in range(2, number + 1):
        for j in range(1, min(number // i + 1, i)):
            divisor[i * j] += 2

    for i in range(1, int(number ** 0.5) + 1):
        divisor[i ** 2] += 1
    # print(divisor)

    for i in range(len(divisor)):
        if divisor[i] > limit:
            divisor[i] = power
    answer = sum(divisor)

    # 시간초과
    # arr = []
    # for i in range(1, number+1):
    #     tmp = 0
    #     for j in range(1, number+1):
    #         if i % j == 0:
    #             tmp += 1
    #     if tmp > limit:
    #         tmp = power
    #     arr.append(tmp)
    # answer = sum(arr)

    return answer