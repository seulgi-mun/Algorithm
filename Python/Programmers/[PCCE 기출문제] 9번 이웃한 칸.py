def solution(board, h, w):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(board)

    for i in range(4):
        nx = dx[i] + w
        ny = dy[i] + h

        if 0 <= nx < n and 0 <= ny < n:
            if board[h][w] == board[ny][nx]:
                answer += 1

    return answer