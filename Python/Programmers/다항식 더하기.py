def solution(polynomial):
    answer = ''

    polynomial = polynomial.split(' + ')

    cnt = 0
    tmp = 0
    for i in polynomial:
        if 'x' in i:
            if i[:len(i) - 1].isdigit():
                cnt += int(i[:len(i) - 1])
            else:
                cnt += 1
        else:
            tmp += int(i)

    if cnt != 0:
        if cnt == 1:
            answer += 'x'
        else:
            answer += str(cnt) + 'x'
    else:
        answer = ''

    if tmp != 0:
        if answer:
            answer += ' + ' + str(tmp)
        else:
            answer += str(tmp)

    return answer
