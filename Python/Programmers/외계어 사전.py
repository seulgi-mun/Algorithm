def solution(spell, dic):
    answer = 0

    spell.sort()

    for i in dic:
        order_i = sorted(i)
        cnt = 0
        for k in spell:
            if k in order_i:
                cnt += 1
        if cnt == len(spell):
            answer = 1
            break
        else:
            answer = 2

    return answer