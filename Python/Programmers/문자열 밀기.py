def solution(A, B):
    answer = 0

    if A == B:
        answer = 0
    else:
        cnt = 0
        # while True:
        for i in range(len(A)):
            if A == B:
                answer = cnt
                break
            else:
                cnt += 1
                f_tmp = A[-1]
                A = f_tmp + A[:len(A) - 1]

        if cnt == len(A):
            answer = -1

    return answer