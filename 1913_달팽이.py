import sys
sys.stdin = open('input.txt')

n = int(input())
f = int(input())

# def snail(n):
#     global s, e
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     arr = [[0] * n for _ in range(n)]
#
#     num = n**2
#     pos = 0
#     x, y = 0, 0
#     arr[x][y] = num
#     num -= 1
#
#     while num > 0:
#         nx = x + dx[pos]
#         ny = y + dy[pos]
#
#         if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
#             arr[nx][ny] = num
#             if num == f:
#                 s, e = nx, ny
#             x, y = nx, ny
#             num -= 1
#         else:
#             pos = (pos+1) % 4
#     return arr
#
# s, e = 0, 0
#
# ans = snail(n)
# # print(ans)
# for i in ans:
#     print(*i)
# print(s+1, e+1)

snail = [[0 for _ in range(n)] for _ in range(n)]

x = (n-1) // 2
y = (n-1) // 2
snail[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

i = 2
s = 3

while x != 0 or y != 0 :
    while i <= s * s:
        if x == y == (n-1) // 2:    # 시작점이면 숫자 설정, 한 칸 위로
            up, down, left, right = s, s-1, s-1, s-2
            x += dx[0]
            y += dy[0]
            up -= 1

        elif right > 0:     # 우
            x += dx[3]
            y += dy[3]
            right -= 1

        elif down > 0:      # 하
            x += dx[1]
            y += dy[1]
            down -= 1

        elif left > 0:      # 좌
            x += dx[2]
            y += dy[2]
            left -= 1

        elif up > 0:        # 상
            x += dx[0]
            y += dy[0]
            up -= 1

        snail[x][y] = i
        i += 1

    n -= 2
    s += 2

for i in range(len(snail)):
    print(*snail[i])
    if f in snail[i]:
        ans_x = i + 1
        ans_y = snail[i].index(f) + 1
print(ans_x, ans_y)