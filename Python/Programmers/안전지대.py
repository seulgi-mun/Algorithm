from collections import deque


def solution(board):
    answer = 0

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    #     def bfs(x, y):
    #         q = deque()
    #         q.append([x, y])
    #         board[x][y] = 1

    #         while q:
    #             # size = len(q)
    #             # for _ in range(size):
    #             t = q.popleft()

    #             for k in range(8):
    #                 nx = t[0] + dx[k]
    #                 ny = t[1] + dy[k]

    #                 if 0 <= nx < len(board) and 0 <= ny < len(board):
    #                     board[nx][ny] = 1
    # return board
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append([i, j])

    for x, y in boom:
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                board[nx][ny] = 1

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1

    return answer