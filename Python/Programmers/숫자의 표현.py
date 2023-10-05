def solution(n):
    answer = 0

    tmp = 0
    num = 1

    while num <= n:
        for i in range(num, n + 1):
            if tmp == n:
                answer += 1
                num += 1
                tmp = 0
                break
            elif tmp > n:
                tmp = 0
                num += 1
                break
            tmp += i

    return answer