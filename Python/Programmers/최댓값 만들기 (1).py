def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            answer.append(numbers[i] * numbers[j])

    return max(answer)