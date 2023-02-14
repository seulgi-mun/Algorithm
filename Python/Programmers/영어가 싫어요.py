def solution(numbers):
    answer = ''

    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
            'nine': '9', }

    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tmp = ''
    for i in numbers:
        tmp += i
        if tmp in num:
            answer += nums[tmp]
            tmp = ''

    return int(answer)