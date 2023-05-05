def solution(n):
    answer = 0
    tmp = ''

    while n > 0:
        n, m = divmod(n, 3)
        tmp += str(m)
    # tmp = tmp[::-1]
    # print(int(tmp, 3))
    answer = int(tmp, 3)
    return answer