def solution(lines):
    answer = 0

    visited = [0] * 200

    for a, b in lines:
        for i in range(a, b):
            visited[i] += 1

    for i in visited:
        if i >= 2:
            answer += 1

    return answer