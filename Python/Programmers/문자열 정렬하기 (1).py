def solution(my_string):
    answer = []

    my_string = sorted(my_string)

    for i in my_string:
        if i.isdigit():
            answer.append(int(i))

    return answer