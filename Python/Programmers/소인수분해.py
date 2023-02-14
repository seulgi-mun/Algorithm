def solution(n):
    answer = []

    tmp = n
    i = 2
    while True:
        if tmp == 1:
            break

        if tmp % i == 0:
            tmp = tmp // i
            if i in answer:
                continue
            answer.append(i)
        else:
            i += 1

    return answer