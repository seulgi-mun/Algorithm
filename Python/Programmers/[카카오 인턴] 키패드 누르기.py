def solution(numbers, hand):
    answer = ''

    le = {1: 'L', 4: 'L', 7: 'L', '*': 'L'}
    ri = {3: 'R', 6: 'R', 9: 'R', '#': 'R'}
    le_com = {2: 'L', 5: 'L', 8: 'L', 0: 'L'}
    ri_com = {2: 'R', 5: 'R', 8: 'R', 0: 'R'}

    pos = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    lx, ly = 3, 0
    rx, ry = 3, 2

    for k in numbers:
        if k in le:
            answer += le[k]
            lx = pos[k][0]
            ly = pos[k][1]
        elif k in ri:
            answer += ri[k]
            rx = pos[k][0]
            ry = pos[k][1]
        else:
            if abs(lx - pos[k][0]) + abs(ly - pos[k][1]) > abs(rx - pos[k][0]) + abs(ry - pos[k][1]):
                answer += ri_com[k]
                rx = pos[k][0]
                ry = pos[k][1]
            elif abs(lx - pos[k][0]) + abs(ly - pos[k][1]) < abs(rx - pos[k][0]) + abs(ry - pos[k][1]):
                answer += le_com[k]
                lx = pos[k][0]
                ly = pos[k][1]
            else:
                if hand == 'right':
                    answer += ri_com[k]
                    rx = pos[k][0]
                    ry = pos[k][1]
                else:
                    answer += le_com[k]
                    lx = pos[k][0]
                    ly = pos[k][1]

    return answer