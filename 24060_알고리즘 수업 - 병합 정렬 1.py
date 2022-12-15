import sys
sys.stdin = open('input.txt')


def merge_sort(a):
    if len(a) == 1:
        return a

    mid = (len(a)+1) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    i, j = 0, 0
    tmp_merge = []
    # print(left, right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp_merge.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            tmp_merge.append(right[j])
            ans.append(right[j])
            j += 1

    # print(tmp_merge)

    while i < len(left):
        tmp_merge.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        tmp_merge.append(right[j])
        ans.append(right[j])
        j += 1
        # print(tmp_merge)
    return tmp_merge

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    # print(ans)
    print(ans[k-1])
else:
    print(-1)

