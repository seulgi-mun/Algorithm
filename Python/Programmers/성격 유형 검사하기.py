def solution(survey, choices):
    answer = ''

    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    kakao = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for j in range(len(choices)):
        if choices[j] < 4:
            kakao[survey[j][0]] += score[choices[j]]
        elif choices[j] > 4:
            kakao[survey[j][1]] += score[choices[j]]
        else:
            continue

    if kakao['R'] > kakao['T']:
        answer += 'R'
    elif kakao['R'] < kakao['T']:
        answer += 'T'
    else:
        answer += 'R'

    if kakao['C'] > kakao['F']:
        answer += 'C'
    elif kakao['C'] < kakao['F']:
        answer += 'F'
    else:
        answer += 'C'

    if kakao['J'] > kakao['M']:
        answer += 'J'
    elif kakao['J'] < kakao['M']:
        answer += 'M'
    else:
        answer += 'J'

    if kakao['A'] > kakao['N']:
        answer += 'A'
    elif kakao['A'] < kakao['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer