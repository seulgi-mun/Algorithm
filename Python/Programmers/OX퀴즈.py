def solution(quiz):
    answer = []

    for i in range(len(quiz)):
        quiz[i] = quiz[i].split(' = ')
        # print(quiz[i])
        for _ in range(len(quiz[i])):
            if '+' in quiz[i][0]:
                quiz[i][0] = quiz[i][0].split(' + ')
                # print(quiz[i][0])
                hap = int(quiz[i][0][0]) + int(quiz[i][0][1])
                if hap == int(quiz[i][1]):
                    answer.append("O")
                else:
                    answer.append("X")
            elif '-' in quiz[i][0]:
                quiz[i][0] = quiz[i][0].split(' - ')
                hap = int(quiz[i][0][0]) - int(quiz[i][0][1])
                # print(hap)
                if hap == int(quiz[i][1]):
                    answer.append("O")
                else:
                    answer.append("X")
    return answer