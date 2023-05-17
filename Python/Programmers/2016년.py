import datetime

def solution(a, b):
    answer = ''
    now = datetime.datetime(2016, a, b)
    answer = now.strftime("%a")

    return answer.upper()
