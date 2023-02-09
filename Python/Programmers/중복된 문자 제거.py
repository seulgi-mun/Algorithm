def solution(my_string):
    answer = ''

    alpha = {}

    for i in my_string:
        if i not in alpha:
            alpha[i] = 1
            answer += i

    # answer = ''.join(alpha)

    return answer