def solution(today, terms, privacies):
    answer = []

    today = list(map(int, today.split('.')))
    days = today[0] * 12 * 28 + today[1] * 28 + today[2]

    term = {}
    for i in terms:
        kind, t = i.split(' ')
        term[kind] = int(t)
    # print(term)
    for idx, val in enumerate(privacies):
        datee, limit = val.split()
        datee = list(map(int, datee.split('.')))

        datee[1] = (datee[1] + term[limit])
        while datee[1] > 12:
            datee[1] -= 12
            datee[0] += 1

        datee[2] -= 1
        if datee[2] == 0:
            datee[2] = 28
            datee[1] -= 1

        # print(datee)
        datee = datee[0] * 12 * 28 + datee[1] * 28 + datee[2]

        if days > datee:
            answer.append(idx + 1)

    #         if today[0] > datee[0]:
    #             answer.append(idx+1)
    #         elif today[0] == datee[0] and today[1] > datee[1]:
    #             answer.append(idx+1)
    #         elif today[0] == datee[0] and today[1] == datee[1] and today[2] > datee[2]:
    #             answer.append(idx+1)

    return answer