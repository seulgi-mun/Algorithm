import sys
sys.stdin = open('input.txt')


def find_duck(x):
    global point
    for k in range(x, len(temp)):
        # duck 움직이면서 확인
        if duck[point % 5] == temp[k] and visited[k] == 0:
            point += 1
            visited[k] = 1


sound = input()

temp = list(sound)
# print(temp)
duck = ['q', 'u', 'a', 'c', 'k']

visited = [0] * len(temp)
cnt = 0
point = 0

if len(temp) % 5 != 0:
    print(-1)
else:
    for i in range(len(temp)):
        # if 'u' in temp or 'a' in temp or 'c' in temp or 'k' in temp:
        # q를 찾았다면 uack 찾아가야됨 그리고 방문하지 않아야 됨
        if temp[i] == 'q' and visited[i] == 0:
            # visited[i] = 1
            # point += 1
            find_duck(i)
            cnt += 1

    if 0 in visited:
        print(-1)
    else:
        print(cnt)

# print(visited)