def solution(arr):
    if len(arr) >= 1:
        arr.remove(min(arr))

    if not arr:
        arr.append(-1)

    return arr