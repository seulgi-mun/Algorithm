def solution(d, budget):
    answer = 0

    d.sort()
    # print(d)
    tmp = 0
    # cnt = 0
    for i in d:
        tmp += i
        if budget >= tmp:
            # print(tmp)
            # tmp += i
            answer += 1

    return answer