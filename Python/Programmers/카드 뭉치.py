def solution(cards1, cards2, goal):
    answer = 'Yes'

    one, two = 0, 0

    for i in range(len(goal)):
        if len(cards1) > one and cards1[one] == goal[i]:
            one += 1
        elif len(cards2) > two and cards2[two] == goal[i]:
            two += 1
        else:
            answer = 'No'
            break

    return answer


# def solution(cards1, cards2, goal):
#     answer = 'Yes'
#
#     word = {}
#
#     for idx, val in enumerate(goal):
#         word[val] = idx
#
#     # print(word)
#
#     if len(cards1) >= 2:
#         for i in range(len(cards1) - 1):
#             if word[cards1[i]] > word[cards1[i + 1]]:
#                 answer += 'No'
#                 break
#             else:
#                 answer += 'Yes'
#     else:
#         if len(cards2) >= 2:
#             for i in range(len(cards2) - 1):
#                 if word[cards2[i]] > word[cards2[i + 1]]:
#                     answer += 'No'
#                     break
#                 else:
#                     answer += 'Yes'
#
#         else:
#             answer += 'Yes'
#
#     if len(cards2) >= 2:
#         for i in range(len(cards2) - 1):
#             if word[cards2[i]] > word[cards2[i + 1]]:
#                 answer += 'No'
#                 break
#             else:
#                 answer += 'Yes'
#
#     else:
#         if len(cards1) >= 2:
#             for i in range(len(cards1) - 1):
#                 if word[cards1[i]] > words[cards1[i + 1]]:
#                     answer += 'No'
#                     break
#                 else:
#                     answer += 'Yes'
#
#         else:
#             answer += 'Yes'
#
#     if 'No' in answer:
#         answer = 'No'
#     else:
#         answer = 'Yes'
#
#     return answer