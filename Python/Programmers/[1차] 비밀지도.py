def solution(n, arr1, arr2):
    total = []

    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        while len(a) < n:
            a = '0' + a
        while len(b) < n:
            b = '0' + b

        tmp = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        total.append(tmp)

    return total

# 한 변 길이 n
# 두 지도에서 겹치는 벽은 벽, 겹치는 공백은 공백