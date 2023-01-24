import sys
sys.stdin = open('input.txt')


n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
# print(time_table)
last_s = max([s for s, e, p in time_table])
# print(last_s)
"""
현재 회의가 끝나는 시간이 제일 늦은 회의 시작 시간보다 크면
더 이상 회의를 할 수 없는 상황이므로 여태까지 회의에 참여한 인원수를 리스트에 추가해준다
"""
tmp = 0
res = []
for i in range(n):
while True:
    tmp += time_table[i][2]
    if time_table[i][1] > last_s:
        res.append(tmp)
        break

    for j in range(i, n):
        if time_table[i][1] > time_table[j][0]:
            continue
        # tmp += time_table[j][2]
    print(tmp)
print(res)