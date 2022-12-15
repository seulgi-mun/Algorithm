import sys
sys.stdin = open('input.txt')

"""
1
2
3
ㅡ ㅡ ㅡ
1 2 3
"""


n = int(input())

def recur(n):

    pass


recur(n)

arr = list(range(n, 0, -1))
top = [[] * (n+1) for _ in range(n+1)]
print(arr)
for i in arr:
    top[1].append(i)
print(top)