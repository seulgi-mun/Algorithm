def solution(nums):
    answer = 0

    arr = []
    res = []

    def recur(cur, s):
        if cur == 3:
            # print(arr)
            tmp = sum(arr)
            res.append(tmp)
            return

        for i in range(s, len(nums)):
            arr.append(nums[i])
            recur(cur + 1, i + 1)
            arr.pop()

    recur(0, 0)

    m = max(res)
    prim = [False, False] + [True] * m

    x = int(m ** 0.5)
    for i in range(2, x + 1):
        if prim[i]:
            for j in range(2 * i, m + 1, i):
                prim[j] = False

    print(prim)
    for i in res:
        # print(i)
        if prim[i]:
            # print(prim[i])
            answer += 1

    return answer