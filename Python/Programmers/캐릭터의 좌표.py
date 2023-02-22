def solution(keyinput, board):
    answer = [0, 0]

    ga = board[0] // 2
    se = board[1] // 2

    for i in keyinput:

        if i == 'left':
            if -board[0] // 2 + 1 < answer[0] - 1 <= board[0] // 2 and -board[1] // 2 + 1 < answer[0] - 1 <= board[
                1] // 2:
                answer[0] = answer[0] - 1
        elif i == 'right':
            if -board[0] // 2 + 1 < answer[0] + 1 <= board[0] // 2 and -board[1] // 2 + 1 < answer[0] + 1 <= board[
                1] // 2:
                answer[0] = answer[0] + 1
        elif i == 'up':

            if -board[0] // 2 + 1 < answer[1] + 1 <= board[0] // 2 and -board[1] // 2 + 1 < answer[1] + 1 <= board[
                1] // 2:
                answer[1] = answer[1] + 1
        else:
            if -board[0] // 2 + 1 < answer[1] - 1 <= board[0] // 2 and -board[1] // 2 + 1 < answer[1] - 1 <= board[
                1] // 2:
                answer[1] = answer[1] - 1
    print(board[0] // 2 + 1)
    return answer