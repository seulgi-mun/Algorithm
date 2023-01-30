import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
tree = list(map(int, input().split()))

def binary_search(tree):
    s = 1
    e = max(tree)

    while s <= e:
        mid = (s+e) // 2
        # print(mid)
        res = 0
        for i in tree:
            if i - mid < 0:
                continue
            res += i-mid
        # print(res)
        if res >= m:
            s = mid + 1
        else:
            e = mid - 1

    return e

print(binary_search(tree))