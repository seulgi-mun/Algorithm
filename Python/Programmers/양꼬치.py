def solution(n, k):
    lamb = n * 12000
    free = n // 10
    drink = (k - free) * 2000
    answer = lamb + drink
    return answer