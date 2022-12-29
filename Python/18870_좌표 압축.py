import sys
sys.stdin = open('input.txt')

"""
좌표 압축 > 여러 곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것
예를 들어, 다음과 같은 좌표가 있다고 하자.
[1, 10, 10000, 1000000]
이렇게 네 점의 좌표가 있을 때, 좌표는 네 개 이지만 좌표값이 1부터 1,000,000 까지 있다.
하지만 이 좌표를 압축하여 순서대로 표현하면 [0, 1, 2, 3] 이 된다.
"""

n = int(input())
x = list(map(int, input().split()))
li_x = sorted(list(set(x)))
# print(li_x, '?')
dic_x = {}


for i in range(len(li_x)):
    dic_x[li_x[i]] = i
# print(dic_x)
for i in x:
    print(dic_x[i], end=' ')