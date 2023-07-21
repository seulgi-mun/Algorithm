def solution(id_list, report, k):
    answer = []

    ban = {}
    vote = {}

    for i in id_list:
        ban[i] = set()
        vote[i] = 0
        # ban[i] = 0

    for i in report:
        key, b = i.split(' ')
        # ban[b] += 1
        ban[b].add(key)
    # print(ban)

    for key, v in ban.items():
        if len(v) >= k:
            # vote[v] += 1
            for vv in v:
                vote[vv] += 1

    return list(vote.values())