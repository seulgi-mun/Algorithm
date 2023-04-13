def solution(n):
    three = 0

    no_three = [0] * (n + 1)
    for i in range(1, n + 1):
        three += 1
        while three % 3 == 0 or '3' in str(three):
            three += 1
        no_three[i] = three

    return no_three[n]