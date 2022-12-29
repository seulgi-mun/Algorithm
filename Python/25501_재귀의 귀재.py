import sys
sys.stdin = open('input.txt')

n = int(input())

def recursion(s, l, r, cnt):
    # print(s, l, r)
    if l >= r:
        cnt += 1
        return 1, cnt
    elif s[l] != s[r]:
        cnt += 1
        return 0, cnt
    else:
        cnt += 1
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)

for _ in range(n):
    word = input()
    print(*isPalindrome(word))
    # print(word, isPalindrome('ABC'))