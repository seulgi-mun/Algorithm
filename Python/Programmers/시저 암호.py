def solution(s, n):
    answer = ''

    tmp = 0
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if i.isupper():
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            else:
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))

    return answer