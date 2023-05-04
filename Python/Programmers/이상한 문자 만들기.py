def solution(s):
    s = s.split()
    # print(s)
    answer = ''

    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer