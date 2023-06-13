def solution(s):
    answer = ''

    s = s.split(' ')

    minn = int(1e9)
    maxx = -int(1e9)

    for i in s:
        if maxx <= int(i):
            maxx = int(i)

        if minn >= int(i):
            minn = int(i)

    answer += str(minn)
    answer += ' '
    answer += str(maxx)

    return answer