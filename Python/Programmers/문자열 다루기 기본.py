def solution(s):
    answer = True

    if 4 == len(s) or len(s) == 6:
        for i in s:
            if i.isdigit() == False:
                answer = False
    else:
        answer = False

    return answer