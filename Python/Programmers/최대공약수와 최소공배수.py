def solution(n, m):
    answer = []

    maxx = 0
    for i in range(1, max(n + 1, m + 1)):
        if n % i == 0 and m % i == 0:
            maxx = i

    answer.append(maxx)
    answer.append(n * m // maxx)

    return answer