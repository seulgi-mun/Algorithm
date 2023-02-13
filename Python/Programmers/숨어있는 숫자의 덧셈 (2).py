def solution(my_string):
    answer = 0

    tmp = ''
    num = []

    for i in my_string:
        if i.isdigit():
            tmp += i
        elif i.isdigit() == False:
            if tmp != '':
                num.append(tmp)
                tmp = ''
    if tmp:
        num.append(tmp)

    for i in num:
        answer += int(i)

    return answer