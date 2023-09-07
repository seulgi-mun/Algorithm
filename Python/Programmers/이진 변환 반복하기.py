def solution(s):
    answer = []

    if s == '1':
        return [0, 0]

    check = 1
    zero = s.count('0')
    one = bin(s.count('1'))[2:]

    while True:
        if one == '1':
            answer.append(check)
            answer.append(zero)
            break

        zero += one.count('0')
        one = bin(one.count('1'))[2:]
        check += 1

    return answer