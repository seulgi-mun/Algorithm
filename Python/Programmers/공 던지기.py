def solution(numbers, k):
    answer = 0

    k = 2 * (k - 1) % len(numbers)

    return numbers[k]