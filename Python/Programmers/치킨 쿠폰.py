def solution(chicken):
    answer = -1

    answer += chicken // 10
    chicken = chicken // 10 + chicken % 10

    while True:
        if chicken < 10:
            answer += 1
            break
        else:
            answer += chicken // 10
            chicken = chicken // 10 + chicken % 10

    return answer