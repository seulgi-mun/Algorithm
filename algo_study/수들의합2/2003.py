import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
num = list(map(int, input().split()))


cnt = 0
find_num = 0
end = 0

for i in range(n):
    # 찾고자 한 부분 값보다 크면 끝점 위치를 옮겨 줌
    while find_num < m and end < n:
        # 위치 옮기면서 값 쌓아 줌
        find_num += num[end]
        # 이동
        end += 1

    # 값이 같으면 다음 시작점부터 값을 찾기위해 현재 시작 값을 빼줌
    if find_num == m:
        cnt += 1
    find_num -= num[i]

print(cnt)