def solution(park, routes):
    h = len(park)
    w = len(park[0])

    ga, se = 0, 0
    for i in range(h):
        for j in range(w):

            if park[i][j] == 'S':
                ga, se = i, j
                break

    go = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for i in routes:
        di, cnt = i.split(' ')
        cnt = int(cnt)
        dx, dy = ga, se

        for _ in range(cnt):
            nx = ga + go[di][0]
            ny = se + go[di][1]

            if 0 <= nx < h and 0 <= ny < w and park[nx][ny] != "X":
                ga, se = nx, ny
            else:
                ga, se = dx, dy
                break

    return (ga, se)