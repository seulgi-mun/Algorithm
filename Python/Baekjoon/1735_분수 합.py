import sys
from fractions import Fraction

sys.stdin = open('input.txt')

a, b = map(int, input().split())
c, d = map(int, input().split())

res = Fraction(a, b) + Fraction(c, d)
print(res.numerator, res.denominator)

# up = (a * d) + (c * b)
# down = b * d

# def gcd(x, y):
#     while y > 0:
#         x, y = y, x % y
#     return x
#
# ja = up // gcd(up, down)
# mo = down // gcd(up, down)
# print(ja, mo)


