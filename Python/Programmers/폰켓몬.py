def solution(nums):
    answer = 0

    new_nums = set(nums)
    if len(nums) // 2 <= len(new_nums):
        answer = len(nums) // 2
    else:
        answer = len(new_nums)

    return answer