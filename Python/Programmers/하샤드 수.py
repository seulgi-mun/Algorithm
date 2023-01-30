def solution(x):
    answer = True

    str_x = str(x)

    tmp = 0
    for i in str_x:
        tmp += int(i)
    # print(tmp)

    if x % tmp != 0:
        answer = False

    return answer