def solution(sizes):
    w = 0
    h = 0

    sizes.sort(key=lambda x: x[0])

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            w = max(w, sizes[i][0])
            h = max(h, sizes[i][1])
        else:
            w = max(w, sizes[i][1])
            h = max(h, sizes[i][0])

    return w * h