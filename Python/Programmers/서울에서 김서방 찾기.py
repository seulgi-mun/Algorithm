def solution(seoul):
    answer = ''

    for k, v in enumerate(seoul):
        if v == 'Kim':
            answer = f'김서방은 {k}에 있다'

    return answer