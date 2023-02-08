def solution(str1, str2):
    answer = 0

    for i in range(len(str1) - len(str2) + 1):
        if str2 == str1[i:len(str2) + i]:
            answer = 1

    if answer == 0:
        answer = 2

    return answer