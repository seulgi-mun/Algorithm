def solution(a, b, n):
    answer = 0

    while True:
        if n < a:
            break

        tmp = n % a
        n = (n // a) * b
        answer += n
        n += tmp

    return answer