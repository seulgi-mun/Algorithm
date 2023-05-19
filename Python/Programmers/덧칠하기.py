def solution(n, m, section):
    answer = 0

    wall = [0] * (n + 1)

    for i in section:
        wall[i] = 1

    s = 0
    e = m

    for i in range(len(wall)):
        if wall[i] == 1:
            s = i
            e = i + m
            if e > len(wall):
                e = len(wall)

            for j in range(s, e):
                if wall[j] == 1:
                    wall[j] = 0
            answer += 1

    # for i in range(1, len(wall), m):
    #     if 1 in wall[i:i+m]:
    #         answer += 1

    return answer