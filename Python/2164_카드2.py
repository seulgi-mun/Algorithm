import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(input())

card = deque(list(range(1, n+1)))


while True:
    if len(card) == 1:
        print(*card)
        break

    # 맨 위 카드 버리기 (pop)
    card.popleft()

    # 제일 위에 카드 밑으로 보내기 (append)
    t = card.popleft()
    card.append(t)
