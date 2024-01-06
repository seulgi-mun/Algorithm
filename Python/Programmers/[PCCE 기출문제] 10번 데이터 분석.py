def solution(data, ext, val_ext, sort_by):
    tmp = []
    for i in range(len(data)):
        if ext == 'code':
            if data[i][0] < val_ext:
                tmp.append(data[i])
        elif ext == 'date':
            if data[i][1] < val_ext:
                tmp.append(data[i])
        elif ext == 'maximum':
            if data[i][2] < val_ext:
                tmp.append(data[i])
        else:
            if data[i][3] < val_ext:
                tmp.append(data[i])

    if sort_by == 'code':
        tmp.sort(key=lambda x: x[0])
    elif sort_by == 'date':
        tmp.sort(key=lambda x: x[1])
    elif sort_by == 'maximum':
        tmp.sort(key=lambda x: x[2])
    else:
        tmp.sort(key=lambda x: x[3])
    # print(tmp)

    return tmp