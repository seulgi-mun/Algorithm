def solution(s):
    s = s.split(' ')
    # print(s)
    answer = ''

    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        if i != len(s) - 1:
            answer += ' '

    return answer