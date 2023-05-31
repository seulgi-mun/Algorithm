def solution(s, skip, index):
    answer = ''

    alpha = []

    for i in range(ord('a'), ord('z') + 1):
        alpha.append(chr(i))
    # print(alpha)

    for i in skip:
        if i in alpha:
            del alpha[alpha.index(i)]

    for i in s:
        tmp = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += tmp

    return answer