def solution(age):
    answer = ''

    alpha = {}
    j = 0
    for i in range(97, 123):
        if chr(i) not in alpha:
            alpha[j] = chr(i)
            j += 1

    for i in str(age):
        answer += alpha[int(i)]

    return answer