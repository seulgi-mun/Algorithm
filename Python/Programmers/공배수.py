def solution(number, n, m):
    answer = 0

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        a = gcd(x, y)
        return (x * y) // a

    b = lcm(n, m)
    # print(b)

    if number % b == 0:
        answer = 1

    return answer