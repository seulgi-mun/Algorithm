def solution(arr):
    stack = []
    for i in range(len(arr)):
        if stack:
            if stack[-1] == arr[i]:
                continue
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])

    return stack