def solution(bin1, bin2):
    answer = ''

    tmp = int(bin1, 2) + int(bin2, 2)

    answer += bin(tmp)[2:]

    return answer