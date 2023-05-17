def solution(answers):
    answer = []

    tmp = ''
    for i in answers:
        tmp += str(i)

    one = '12345'
    two = '21232425'
    three = '3311224455'

    res = [0, 0, 0]

    for i in range(len(tmp)):
        if tmp[i] == one[i % len(one)]:
            res[0] += 1
        if tmp[i] == two[i % len(two)]:
            # print(tmp[i])
            res[1] += 1
        if tmp[i] == three[i % len(three)]:
            # print(tmp[i])
            res[2] += 1

    maxx = max(res)

    for i in range(len(res)):
        if res[i] == maxx:
            answer.append(i + 1)
    answer.sort()

    return answer