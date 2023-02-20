def solution(sides):
    answer = 0

    sides.sort()

    for i in range(1, sum(sides)):
        if max(sides) - min(sides) < i <= max(sides):
            answer += 1
            if i + min(sides) < sum(sides):
                answer += 1

    return answer