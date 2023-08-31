def solution(new_id):
    answer = ''

    #   조건 1
    new_id = new_id.lower()

    #   조건 2
    for i in new_id:
        if i not in 'abcdefghijklnmopqrstuvwxyz0123456789-_.':
            new_id = new_id.replace(i, '')

    #   조건 3
    point = 0
    tmp = ''
    for i in range(len(new_id) - 1):
        if new_id[i] == '.' and new_id[i + 1] == '.':
            point += 1
        else:
            if point >= 2:
                tmp += '.'
                point = 0
            else:
                tmp += new_id[i]

    if new_id[-1] == '.':
        if point >= 2:
            tmp += '.'
            point = 0
        else:
            tmp += new_id[-1]
    else:
        tmp += new_id[-1]

    # 조건 4
    tmp = tmp.lstrip('.')
    tmp = tmp.rstrip('.')

    # 조건 5
    if tmp == '':
        tmp = 'a'

    # 조건 6
    new = ''
    if len(tmp) >= 16:
        for i in range(15):
            # print(tmp[i])
            new += tmp[i]
    else:
        new = tmp
    new = new.rstrip('.')

    # 조건 7
    while True:
        if new != '':
            if len(new) <= 2:
                new += new[-1]
            else:
                break
        else:
            new += 'a'

    return new