from pprint import pprint


def solution(board, moves):
    answer = 0

    stack = []

    n = len(board)

    for j in moves:
        for i in range(n):
            if board[i][j - 1] != 0:
                stack.append(board[i][j - 1])
                board[i][j - 1] = 0
                # break
            else:
                continue

            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
            break
    return answer