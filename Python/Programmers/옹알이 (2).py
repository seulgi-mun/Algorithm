def solution(babbling):
    answer = 0

    say = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in say:
            if j * 2 not in i:
                i = i.replace(j, ' ')
                print(j * 2)
        if i.strip() == '':
            answer += 1
    return answer