import sys, math
sys.stdin = open('input.txt')

n, m = map(int, input().split())


numerator = math.factorial(n)
denominator = (math.factorial(n-m)) * (math.factorial(m))
print(numerator // denominator)

# def fac(n):
#     num = 1
#
#     for i in range(2, n+1):
#         num *= i
#     return num
#
# print(fac(n) // (fac(m) * fac(n-m)))
