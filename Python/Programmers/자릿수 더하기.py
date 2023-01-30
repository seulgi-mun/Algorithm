def solution(n):
    answer = 0

    str_n = str(n)
    # print(str_n)
    for i in str_n:
        answer += int(i)

    return answer