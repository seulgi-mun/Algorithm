def solution(numbers):
    answer = []

    arr = []

    def recur(cur, s):
        if cur == 2:
            tmp = sum(arr)
            if tmp not in answer:
                answer.append(tmp)
            return

        for i in range(s, len(numbers)):
            arr.append(numbers[i])
            recur(cur + 1, i + 1)
            arr.pop()

    recur(0, 0)
    answer.sort()
    return answer