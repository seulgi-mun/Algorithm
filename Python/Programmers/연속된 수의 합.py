def solution(num, total):
    answer = [0] * num

    s = (total // num) - ((num - 1) // 2)

    for i in range(num):
        answer[i] = s
        s += 1

    return answer