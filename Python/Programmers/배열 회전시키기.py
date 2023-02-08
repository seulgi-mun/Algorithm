def solution(numbers, direction):
    answer = []

    if direction == 'right':
        answer.append(numbers.pop())
        for i in range(len(numbers)):
            answer.append(numbers[i])
    else:
        tmp = numbers.pop(0)
        for i in range(len(numbers)):
            answer.append(numbers[i])
        answer.append(tmp)

    return answer