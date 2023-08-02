def solution(n, lost, reserve):
    answer = 0

    s_lost = set(lost)
    s_reserve = set(reserve)

    giver = s_reserve - s_lost
    getter = s_lost - s_reserve

    for i in giver:
        if i - 1 in getter:
            getter.remove(i - 1)
        elif i + 1 in getter:
            getter.remove(i + 1)
    answer = n - len(getter)
    return answer